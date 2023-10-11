from time import sleep, time
from typing import Union

from PyPDF2 import PdfReader
from selene.api.shared import browser

import config
from utils.assertion.soft_assertions import soft_assert


def get_downloaded_filename(timeout=20):
    driver = browser.driver
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get("chrome://downloads")
    sleep(6)
    end_time = time() + timeout
    while True:
        filename = (
            config.settings.download_dir
            + "/"
            + driver.execute_script(
                "return document.querySelector('downloads-manager').shadowRoot."
                "querySelector('#downloadsList downloads-item').shadowRoot."
                "querySelector('div#content  #file-link').text"
            )
        )
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        if filename:
            return filename
        sleep(1)
        if time() > end_time:
            return None


def verify_text_in_pdf(filename, text: Union[str, list], expected=True) -> None:
    doc_text = __read_pdf_file(filename)
    if isinstance(text, list):
        for item in text:
            text_found = doc_text.find(item) >= 0
            soft_assert(
                text_found == expected,
                error_message=f"Text '{item} could not be found within pdf file {filename}",
            )
    else:
        text_found = doc_text.find(text) >= 0
        soft_assert(
            text_found == expected,
            error_message=f"Text '{text} could not be found within pdf file {filename}",
        )


def __read_pdf_file(filename):
    pdf_reader = PdfReader(filename)
    doc_text = ""
    for page in pdf_reader.pages:
        doc_text += page.extract_text()
    return doc_text


def file_is_valid_pdf(filename):
    doc_text = __read_pdf_file(filename)
    return doc_text is not None
