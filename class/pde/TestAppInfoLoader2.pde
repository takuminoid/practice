//Test AppInfoLoader class
private final String TARGET_CLASS_NAME  = "AppInfoLoader";
private final String TARGET_CLASS_NAME2 = "AppInfoLoader2";
private final String SOME_TROUBLE       = "Some trouble happend.";
private final String TARGET_CLASS_VERSION = "1.0";

void setup(){
  test();
}

void test(){
  noLoop();
  println("Test Start.");
  println("...AppInfoLoader begins.");
  assert AppInfoLoader.CLASS_NAME.equals(TARGET_CLASS_NAME)
         : TARGET_CLASS_NAME + " : " + SOME_TROUBLE;  
  AppInfoLoader ail = new AppInfoLoader();
  assert ail.CLASS_NAME.equals(TARGET_CLASS_NAME)
         : TARGET_CLASS_NAME + " : " + SOME_TROUBLE;
  assert ail.getVersion().equals(TARGET_CLASS_VERSION)
         : TARGET_CLASS_NAME + " : " + SOME_TROUBLE
            + "(" + ail.getVersion() + ")";
  println("...AppInfoLoader finished.");

  println("...AppInfoLoader2 begins");
  assert AppInfoLoader2.CLASS_NAME.equals(TARGET_CLASS_NAME2)
         : TARGET_CLASS_NAME2 + " : " + SOME_TROUBLE;  
  AppInfoLoader2 ail2 = new AppInfoLoader2();
  assert ail2.CLASS_NAME.equals(TARGET_CLASS_NAME2)
         : TARGET_CLASS_NAME2 + " : " + SOME_TROUBLE;
  
  assert ail2.getVersion().equals(TARGET_CLASS_VERSION)
         : TARGET_CLASS_NAME2 + " : " +   SOME_TROUBLE
           + "(" + ail2.getVersion() + ")";
  println("...AppInfoLoader2 finished.");
  println("All Test Done.");
  exit();
}
