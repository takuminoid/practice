import app_info_loader

TARGET_CLASS_NAME = "AppInfoLoader"
SOME_TROUBLE = TARGET_CLASS_NAME + " : " + "Some trouble happend."
TARGET_CLASS_VERSION = "1.0"

if __name__ == "__main__":
    ail = app_info_loader.AppInfoLoader()
    print("Test Start.")

    ail.app_info_loader()
    assert ail.CLASS_NAME == TARGET_CLASS_NAME
    assert ail.get_version() == TARGET_CLASS_VERSION

    print("All Test Done")
