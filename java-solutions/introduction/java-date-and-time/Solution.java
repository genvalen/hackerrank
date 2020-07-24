// https://www.hackerrank.com/challenges/java-date-and-time/problem

class Result {

    public static String findDay(int month, int day, int year) {
    /*program creates string array, and uses 
    *Day_OF_WEEK (calendar field returning int value) 
    *to determine which index holds correct date. 
    */
        String [] DAYS = new String[] {"SUNDAY","MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"};
        Calendar cal = Calendar.getInstance(Locale.US);
        cal.set(year, month-1, day); //Month fields start at 0, subract 1.
        int dayOfWeek = cal.get(cal.DAY_OF_WEEK) - 1; //DAY_OF_WEEK fields start at 1, subract 1.
        return DAYS[dayOfWeek];
    }
}
