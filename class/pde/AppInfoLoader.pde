public class AppInfoLoader{
  public static final String CLASS_NAME = "AppInfoLoader";
  private static final String CONFIG_FILENAME = "CONFIG.TXT";
  
  private String version;
  
  public AppInfoLoader(){
    String lines[] = loadStrings(CONFIG_FILENAME);
    if (0 < lines.length){
      version = "No Info";
      for(String v : lines){
        String[] tokens = split(v, ",");
        if(tokens[0].equals("VERSION")){
          version = tokens[1];
        }
      }
    }
  }
  
  public String getVersion(){
    return version;
  }
}
