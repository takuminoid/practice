//Test AppInfoLoader class
private final String TARGET_CLASS_NAME4 = "AppInfoLoader4";
private final String TARGET_CLASS_NAME5 = "AppInfoLoader5";
private final String SOME_TROUBLE       = "Some trouble happend.";
private final String TARGET_CLASS_VERSION = "1.0";

void setup(){
  test();
}

void test(){
  noLoop();
  println("Test Start.");
  
  ConfigInfo a = new AppInfoLoader4();
  testAppInfoLoader(a, TARGET_CLASS_NAME4, TARGET_CLASS_VERSION);
  a = new AppInfoLoader5();
  testAppInfoLoader(a, TARGET_CLASS_NAME5, TARGET_CLASS_VERSION);
  
  println("All Test Done.");
  exit();
}

void testAppInfoLoader(ConfigInfo c, String name, String ver){
  println("..." + c.getClassName() + " begins");
  assert c.getClassName().equals(name) : name + " : " + SOME_TROUBLE;
  assert c.getVersion().equals(ver) : name + " : " + SOME_TROUBLE + "(" + c.getVersion() + ")";
  println("..." + c.getClassName() + " finished.");
}
