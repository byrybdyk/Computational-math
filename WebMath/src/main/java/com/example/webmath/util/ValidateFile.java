package com.example.webmath.util;


public class ValidateFile {


    public boolean validateFile(String[] lines) {
        String num1 = lines[0].trim();
        int num2,num3;
        float num4,num5,num6;
        if(lines.length !=6){
            return false;
        }
        if (!(num1.equals("true") || num1.equals("false"))) {
            System.out.println("failed true");
            return false;
        }
        try{
            num2 = Integer.parseInt(lines[1].trim());
            num3 = Integer.parseInt(lines[2].trim());
            num4 = Float.parseFloat(lines[3].trim());
            num5 = Float.parseFloat(lines[4].trim());
            num6 = Float.parseFloat(lines[5].trim());
        } catch (NumberFormatException e){
            System.out.println("Failed to convert");
            return false;
        }
        if (lines[0].equals("true")) {
                if ( 3 < num2 || num2 <1){
                    return false;
                }
                if (3 < num3 || num3 <1){
                    return false;
                }
        }
        if (lines[0].equals("false")) {
            if ( 2 < num2 || num2 <1){
                return false;
            }
            if (num3 != 1){
                return false;
            }
        }
        if(num6 <0){
            return false;
        }


        return true;
    }
}
