public class AppInfoLoader5 implements ConfigInfo{
  public static final String CLASS_NAME = "AppInfoLoader5";
  private static final String CONFIG_FILENAME = "CONFIG.TXT";
  
  private String version;
  
  public AppInfoLoader5(){
    try {
      BufferedReader br = createReader(CONFIG_FILENAME);
      version = "No Info";
      String line = br.readLine();
      while(line != null){
        String[] tokens = split(line, ",");
        if(tokens[0].equals("VERSION")){
          version = tokens[1];
        }
        line = br.readLine();
      }
    } catch(IOException e){
      e.printStackTrace();
    }
  }
  
  public String getVersion(){
    return version;
  }
  public String getClassName(){
    return CLASS_NAME;
  }
}
