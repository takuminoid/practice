class AppInfoLoader:
    """
    classの説明を記載します
    """

    def __init__(self):
        """
        コンストラクタ

        Args:
          引数名:引数の説明
        """

        # Private Member
        self.__version = ""
        self.CONFIG_FILENAME = "CONFIG.TXT"


    #---------------------------------------
    # クラス定数
    #---------------------------------------
    CLASS_NAME = "AppInfoLoader"
    


    #---------------------------------------
    # public関数
    #---------------------------------------
    def app_info_loader(self):
        """
        publicクラスメソッドを定義します

        Args:
          引数名:引数の説明

        Returns:
          戻り値の説明

        Raises:
          例外型：発生する条件の説明
        """
        lines = self.__load_string(self.CONFIG_FILENAME)
        if 0 < len(lines):
            version = "No info"
            for v in lines:
                tokens = v.split(",")
                if tokens[0] == "VERSION":
                    self.__version = tokens[1]

    def get_version(self):
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

    #---------------------------------------
    # private methods
    #---------------------------------------
    def __load_string(self, file_name):
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
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # 改行文字を含む場合は、改行文字を削除する
        lines = [line.strip() for line in lines]
        return lines