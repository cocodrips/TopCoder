public class InsertZ {
 
    public String canTransform(String init, String goal) {
        String ansString = goal.replaceAll("z", "");
        if (ansString.equals(init)) {
            return "Yes";
        }
        return "No";
    }
 
}