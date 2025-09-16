from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import time
import os
import base64
from pytest_html import extras



@pytest.fixture()
def driver(request):
    #found the browser|
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver ")
    
    if browser == "chrome":
        service = Service("/usr/bin/chromedriver") 
        my_driver = webdriver.Chrome(service=service)
          
    elif browser == "firefox":
        my_driver= webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError (f"Expected chrome  or firefox, but got {browser} ")
    
    #add yield if u want return something and keep write code in the same function
    #my_driver.implicitly_wait(10)
    yield my_driver
    print (f"Closing {browser} driver") 
    
    my_driver.quit()
    
def pytest_addoption(parser):
    parser.addoption(
    "--browser", action="store", default="chrome", help="browser to excute test(chrome or firefox)")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook que guarda screenshot y lo adjunta al reporte HTML.
    Guarda la imagen en: <project>/test/reports/assets/<filename>.png
    Y agrega al report.extra tanto la versión embebida (base64) como la ruta relativa
    (la que use report.html para cargar assets/archivo.png si no usas --self-contained-html).
    """
    outcome = yield
    report = outcome.get_result()

    # obtener driver usado por el test (si existe)
    driver = item.funcargs.get("driver", None)

    # solo nos interesa la fase "call" y si hay driver
    if report.when != "call" or driver is None:
        return

    # directorios (basados en el cwd del proyecto)
    cwd = os.getcwd()
    report_dir = os.path.join(cwd, "test", "reports")      # donde está report.html
    assets_dir = os.path.join(report_dir, "assets")        # carpeta assets junto al report

    # crear carpeta assets si no existe
    os.makedirs(assets_dir, exist_ok=True)

    # nombre único del archivo
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    status = "failed" if report.failed else "passed"
    filename = f"{item.name}_{status}_{timestamp}.png"

    abs_path = os.path.join(assets_dir, filename)   # ruta absoluta para guardar el .png

    saved = False
    try:
        saved = driver.save_screenshot(abs_path)   # devuelve True si guardó
        print(f"[screenshot] Guardado en: {abs_path} (saved={saved})")
    except Exception as e:
        print("[screenshot] Error al guardar:", e)
        saved = False

    # Si se guardó correctamente, preparar los extras para pytest-html
    if saved:
        # 1) ruta relativa desde report_dir (report.html) -> ej: "assets/archivo.png"
        rel_path = os.path.relpath(abs_path, start=report_dir)

        # 2) crear extra para la ruta (archivo externo)
        extra_file = None
        try:
            extra_file = extras.image(rel_path, mime_type="image/png")
        except Exception as e:
            print("[screenshot] extra_file error:", e)
            extra_file = None

        # 3) crear extra embebido en base64 (funciona siempre con --self-contained-html)
        extra_b64 = None
        try:
            with open(abs_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("utf-8")
            extra_b64 = extras.image(b64, mime_type="image/png", extension="png")
        except Exception as e:
            print("[screenshot] extra_b64 error:", e)
            extra_b64 = None

        # Añadir preferentemente la versión embebida (si existe), y también la de archivo
        extras_to_add = []
        if extra_b64:
            extras_to_add.append(extra_b64)
        if extra_file:
            extras_to_add.append(extra_file)

        if extras_to_add:
            if hasattr(report, "extra"):
                report.extra.extend(extras_to_add)
            else:
                report.extra = extras_to_add

    # Forzamos que pytest use este report modificado (asegura que pytest-html lo lea)
    outcome.force_result(report)



 