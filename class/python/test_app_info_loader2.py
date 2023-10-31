import app_info_loader4

TARGET_CLASS_NAME = "AppInfoLoader4"
SOME_TROUBLE = "Some trouble happened."
TARGET_CLASS_VERSION = "1.0"

if __name__ == "__main__":
    print("Test Start.")

    print("...AppInfoLoader4 begins")
    assert app_info_loader4.AppInfoLoader4.CLASS_NAME == TARGET_CLASS_NAME, (
        TARGET_CLASS_NAME + " : " + SOME_TROUBLE
    )
    ail4 = app_info_loader4.AppInfoLoader4()
    ail4.app_info_loader4()
    assert ail4.CLASS_NAME == TARGET_CLASS_NAME, (
        TARGET_CLASS_NAME + " : " + SOME_TROUBLE
    )
    assert ail4.get_class_name() == TARGET_CLASS_NAME, (
        TARGET_CLASS_NAME + " : " + SOME_TROUBLE
    )
    assert ail4.get_version() == TARGET_CLASS_VERSION, (
        TARGET_CLASS_NAME + " : " + SOME_TROUBLE + "(" + ail4.get_version() + ")"
    )
    print("...AppInfoLoader4 finished.")

    print("All Test Done.")
