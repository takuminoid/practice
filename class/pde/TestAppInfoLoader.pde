//Test AppInfoLoader class
private final String TARGET_CLASS_NAME = "AppInfoLoader";
private final String SOME_TROUBLE = TARGET_CLASS_NAME + " : "
                                  + "Some trouble happend.";
private final String TARGET_CLASS_VERSION = "1.0";

void setup(){
  test();
}

void test(){
  noLoop();
  println("Test Start.");
  
  assert AppInfoLoader.CLASS_NAME.equals(TARGET_CLASS_NAME)
       : SOME_TROUBLE;  
  AppInfoLoader ail = new AppInfoLoader();
  assert ail.CLASS_NAME.equals(TARGET_CLASS_NAME)
       : SOME_TROUBLE;
  assert ail.getVersion().equals(TARGET_CLASS_VERSION)
       : SOME_TROUBLE + ail.getVersion();
  println("All Test Done.");
  exit();
}
