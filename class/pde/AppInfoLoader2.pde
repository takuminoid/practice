public class AppInfoLoader2{
  public static final String CLASS_NAME = "AppInfoLoader2";
  private static final String CONFIG_FILENAME = "CONFIG.TXT";
  
  private String version;
  
  public AppInfoLoader2(){
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
}
