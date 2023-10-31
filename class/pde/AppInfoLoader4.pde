public class AppInfoLoader4 implements ConfigInfo{
  public static final String CLASS_NAME = "AppInfoLoader4";
  
  private String version;
  
  public AppInfoLoader4(){
    String lines[] = loadStrings(CONFIG_FILENAME);
    if (0 < lines.length){
      version = "No Version Info(Config file contains " + lines.length + " lines but...)";
      for(String v : lines){
        String[] tokens = split(v, ",");
        if(tokens[0].equals("VERSION")){
          version = tokens[1];
        }
      }
    } else {
      version = "No Info";
    }
  }
  
  public String getVersion(){
    return version;
  }
  public String getClassName(){
    return CLASS_NAME;
  }
}
