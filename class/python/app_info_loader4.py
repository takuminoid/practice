import config_info


class AppInfoLoader4(config_info.ConfigInfo):
    def __init__(self):
        """
        コンストラクタ

        Args:
          引数名:引数の説明
        """

        # Private Member
        self.__version = ""

    # ---------------------------------------
    # クラス定数
    # ---------------------------------------
    CLASS_NAME = "AppInfoLoader4"
    CONFIG_FILENAME = "CONFIG.TXT"

    # ---------------------------------------
    # public関数
    # ---------------------------------------
    def app_info_loader4(self):
        """
        publicクラスメソッドを定義します

        Args:
          引数名:引数の説明

        Returns:
          戻り値の説明

        Raises:
          例外型：発生する条件の説明
        """
        lines = self.__load_string(AppInfoLoader4.CONFIG_FILENAME)
        if 0 < len(lines):
            version = (
                "No Version Info(Config file contains "
                + str(len(lines))
                + " lines but..."
            )
            for v in lines:
                tokens = v.split(",")
                if tokens[0] == "VERSION":
                    self.__version = tokens[1]
        else:
            self.__version = "No Info"

    def get_version(self) -> str:
        """
        public関数を定義します

        Args:
          引数名:引数の説明

        Returns:
          戻り値の説明

        Raises:
          例外型：発生する条件の説明
        """
        return self.__version

    def get_class_name(self) -> str:
        """
        public関数を定義します

        Args:
          引数名:引数の説明

        Returns:
          戻り値の説明

        Raises:
          例外型：発生する条件の説明
        """
        return self.CLASS_NAME

    # ---------------------------------------
    # private methods
    # ---------------------------------------
    def __load_string(self, file_name: str) -> list:
        """
        private関数を定義します

        Args:
          引数名:引数の説明

        Returns:
          戻り値の説明

        Raises:
          例外型：発生する条件の説明
        """
        # ファイルを読み込む
        with open(file_name, "r") as file:
            lines = file.readlines()

        # 改行文字を含む場合は、改行文字を削除する
        lines = [line.strip() for line in lines]
        return lines
