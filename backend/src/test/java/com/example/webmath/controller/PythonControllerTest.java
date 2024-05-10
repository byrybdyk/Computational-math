package com.example.webmath.controller;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class PythonControllerTest {
    
    private final PythonController pythonController = new PythonController();
        private String Lab4Test(String pair1, String pair2, String pair3, String pair4, String pair5, String pair6, String pair7, String pair8, String pair9, String pair10, String pair11, String pair12) {
                String result ="";
                // String pair1 = "2 2", pair2 = "3 3", pair3 = "4 4", pair4 = "5 5", pair5 = "6 6", pair6 = "7 7", pair7 = "8 8", pair8 = "9 9",pair9="", pair10 = "", pair11 = "", pair12 = "";
                
                try {
                    String currentDir = System.getProperty("user.dir");
                    String scriptPath;
                    String launchCommand;
                    String osName = System.getProperty("os.name").toLowerCase();
                    if (osName.contains("windows")) {
                        scriptPath = currentDir + "\\src\\main\\resources\\scripts\\lb4\\main.py";
                        launchCommand = "python";
                    } else {
                        scriptPath = "../../main/resources/scripts/lb4/main.py";
                        launchCommand = "python3";
                    }

                    ProcessBuilder processBuilder = new ProcessBuilder(launchCommand, scriptPath, pair1, pair2, pair3, pair4, pair5, pair6, pair7, pair8, pair9, pair10, pair11, pair12);
                    Process process = processBuilder.start();

                    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                    StringBuilder output = new StringBuilder();
                    String line;
                    while ((line = reader.readLine()) != null) {
                        output.append(line).append("\n");
                    }
                    result = output.toString();
                    System.out.println(result);
                    int exitCode = process.waitFor();

                }catch (IOException | InterruptedException e) {
                }
                return result;
            }

            private String Lab3Test(String quation, String method, String leftBorder, String rightBorder, String inaccuary, String parts) {
                String result ="";
                // String pair1 = "2 2", pair2 = "3 3", pair3 = "4 4", pair4 = "5 5", pair5 = "6 6", pair6 = "7 7", pair7 = "8 8", pair8 = "9 9",pair9="", pair10 = "", pair11 = "", pair12 = "";
                
                try {
                    String currentDir = System.getProperty("user.dir");
                    String scriptPath;
                    String launchCommand;
                    String osName = System.getProperty("os.name").toLowerCase();
                    if (osName.contains("windows")) {
                        scriptPath = currentDir + "\\src\\main\\resources\\scripts\\lb3\\main.py";
                        launchCommand = "python";
                    } else {
                        scriptPath = "../../main/resources/scripts/lb3/main.py";
                        launchCommand = "python3";
                    }
                    ProcessBuilder processBuilder = new ProcessBuilder(launchCommand, scriptPath, quation, method, leftBorder, rightBorder,inaccuary, parts);
                    Process process = processBuilder.start();

                    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                    StringBuilder output = new StringBuilder();
                    String line;
                    while ((line = reader.readLine()) != null) {
                        output.append(line).append("\n");
                    }
                    result = output.toString();
                    System.out.println(result);
                    int exitCode = process.waitFor();

                }catch (IOException | InterruptedException e) {
                }
                return result;
            }

            private String Lab2Test( String type,String quation, String method, String leftBorder, String rightBorder, String inaccuary) {
                String result ="";
                // String pair1 = "2 2", pair2 = "3 3", pair3 = "4 4", pair4 = "5 5", pair5 = "6 6", pair6 = "7 7", pair7 = "8 8", pair8 = "9 9",pair9="", pair10 = "", pair11 = "", pair12 = "";
                
                try {
                    String currentDir = System.getProperty("user.dir");
                    String scriptPath;
                    String launchCommand;
                    String osName = System.getProperty("os.name").toLowerCase();
                    if (osName.contains("windows")) {
                        scriptPath = currentDir + "\\src\\main\\resources\\scripts\\lb2\\main.py";
                        launchCommand = "python";
                    } else {
                        scriptPath = "../../main/resources/scripts/lb2/main.py";
                        launchCommand = "python3";
                    }
                    ProcessBuilder processBuilder = new ProcessBuilder(launchCommand, scriptPath, type, quation, method, leftBorder, rightBorder,inaccuary);

                    Process process = processBuilder.start();

                    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                    StringBuilder output = new StringBuilder();
                    String line;
                    while ((line = reader.readLine()) != null) {
                        output.append(line).append("\n");
                    }
                    result = output.toString();
                    System.out.println(result);
                    int exitCode = process.waitFor();

                }catch (IOException | InterruptedException e) {
                }
                return result;
            }
        @Test
        public void testRunPythonLab4Script_Success() {
            String result1 = Lab4Test("2 2", "3 3", "4 4", "5 5", "6 6", "7 7", "8 8", "9 9", "", "", "", "");
            String answer1 ="P1(x) = 1.0x + 0.0zzP1(x) = 0x^2 + 1x + 0zzP1(x) = 0.00020879882498145205x^3 + 0.12766556727437353x^2 + -0.4252011225162542x + 3.25365243287883zzP1(x) = 4.642652787836518ln(x) + -1.9293050049752978zzP1(x) = 0.20588ln(x) + 0.4678925624267294zzP1(x) = 1.0ln(x) + 0.0zzspace\n" + //
                "Best quation is P1(x) = 1.0x + 0.0 with S2 = 0.0\n" + //
                "Linear\n" + //
                "P1(x) = 1.0x + 0.0\n" + //
                "fi = 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0,\n" + //
                "Pirson = 1.0\n" + //
                "S = 0.0\n" + //
                "S2 = 0.0\n" + //
                "ei = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\n" + //
                "Pi = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\n" + //
                "Quadratic\n" + //
                "P1(x) = 0x^2 + 1x + 0\n" + //
                "fi = 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0,\n" + //
                "\n" + //
                "S = 0.0\n" + //
                "S2 = 0.0\n" + //
                "ei = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\n" + //
                "Pi = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\n" + //
                "Qubic\n" + //
                "P1(x) = 0.00020879882498145205x^3 + 0.12766556727437353x^2 + -0.4252011225162542x + 3.25365243287883\n" + //
                "fi = 2.915582847543667, 3.1326767390739283, 3.6088601440026027, 4.345385855279578, 5.343506665854746, 6.604475368677991, 8.129544756699206, 9.919967622868276,\n" + //
                "S = 2.8879506360989007\n" + //
                "S2 = 0.6008276204639419\n" + //
                "ei = 0.9155828475436669, 0.1326767390739283, -0.3911398559973973, -0.6546141447204219, -0.6564933341452539, -0.3955246313220089, 0.12954475669920562, 0.9199676228682758,\n" + //
                "Logarithmic\n" + //
                "P1(x) = 4.642652787836518ln(x) + -1.9293050049752978\n" + //
                "fi = 1.2887366852323545, 3.1711703997611593, 4.506778375440007, 5.542756406036664, 6.389212089968812, 7.104880173415726, 7.724820065647657, 8.271645804497616,\n" + //
                "Pirson = 0.9776634758086947\n" + //
                "S = 1.8553133789257892\n" + //
                "S2 = 0.4815746799466555\n" + //
                "ei = -0.7112633147676455, 0.17117039976115933, 0.5067783754400068, 0.5427564060366636, 0.3892120899688116, 0.10488017341572586, -0.27517993435234267, -0.7283541955023836,\n" + //
                "Pi = -0.35563165738382274, 0.057056799920386446, 0.1266945938600017, 0.10855128120733273, 0.0648686816614686, 0.014982881916532267, -0.034397491794042834, -0.08092824394470928,\n" + //
                "Exp\n" + //
                "P1(x) = 0.20588ln(x) + 0.4678925624267294\n" + //
                "fi = 0.8796510615479856, 1.0855303111086136, 1.2914095606692417, 1.4972888102298698, 1.703168059790498, 1.909047309351126, 2.114926558911754, 2.3208058084723824,\n" + //
                "Pirson = 0.9776634758086947\n" + //
                "S = 0.08227419615651133\n" + //
                "S2 = 0.10141141217616445\n" + //
                "ei = 0.18650388098804027, -0.013081977559496138, -0.09488480045064884, -0.11214910220423047, -0.08859140943755706, -0.036862839704187245, 0.0354850172319181, 0.12358123113616282,\n" + //
                "Pi = 0.26906822420799115, -0.011907729136505407, -0.06844491553294499, -0.06968215507898476, -0.04944380702825305, -0.018943752219023658, 0.017064686128782553, 0.05624424212748663,\n" + //
                "Gradual\n" + //
                "P1(x) = 1.0ln(x) + 0.0\n" + //
                "fi = 0.6931471805599453, 1.0986122886681098, 1.3862943611198906, 1.6094379124341003, 1.791759469228055, 1.9459101490553132, 2.0794415416798357, 2.1972245773362196,\n" + //
                "Pirson = 1.0\n" + //
                "S = 0.0\n" + //
                "S2 = 0.0\n" + //
                "ei = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\n" + //
                "Pi = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\n";
            assertEquals(result1,answer1);
        
        

            String result2 = Lab4Test("2 4", "3 9", "4 16", "5 25", "6 36", "7 49", "8 64", "9 81", "", "", "", "");
            String answer2 ="P1(x) = 11.000000000000002x + -25.00000000000001zzP1(x) = 1x^2 + 0x + 0zzP1(x) = 0.0002215622947824248x^3 + -0.13465216333719496x^2 + 12.459017567230902x + -28.300500081879495zzP1(x) = 49.140617215183795ln(x) + -43.13621298168807zzP1(x) = 0.41176ln(x) + 0.9357851248534588zzP1(x) = 2.0ln(x) + 0.0zzspace\n" + //
                            "Best quation is P1(x) = 1x^2 + 0x + 0 with S2 = 0.0\n" + //
                            "Linear\n" + //
                            "P1(x) = 11.000000000000002x + -25.00000000000001\n" + //
                            "fi = -3.000000000000007, 7.9999999999999964, 18.999999999999996, 29.999999999999996, 41.0, 52.0, 63.0, 74.0,\n" + //
                            "Pirson = 0.9838699100999075\n" + //
                            "S = 168.00000000000006\n" + //
                            "S2 = 4.582575694955841\n" + //
                            "ei = -7.000000000000007, -1.0000000000000036, 2.9999999999999964, 4.9999999999999964, 5.0, 3.0, -1.0, -7.0,\n" + //
                            "Pi = -1.7500000000000018, -0.11111111111111151, 0.18749999999999978, 0.19999999999999984, 0.1388888888888889, 0.061224489795918366, -0.015625, -0.08641975308641975,\n" + //
                            "Quadratic\n" + //
                            "P1(x) = 1x^2 + 0x + 0\n" + //
                            "fi = 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0,\n" + //
                            "\n" + //
                            "S = 0.0\n" + //
                            "S2 = 0.0\n" + //
                            "ei = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\n" + //
                            "Pi = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\n" + //
                            "Qubic\n" + //
                            "P1(x) = 0.0002215622947824248x^3 + -0.13465216333719496x^2 + 12.459017567230902x + -28.300500081879495\n" + //
                            "fi = -3.919301102408212, 7.870665331737581, 19.39531556051507, 30.655978957692945, 41.653984897039905, 52.39066275232464, 62.867341897315846, 73.08535170578222,\n" + //
                            "S = 214.89770358358203\n" + //
                            "S2 = 5.182876898783894\n" + //
                            "ei = -7.9193011024082125, -1.1293346682624188, 3.395315560515069, 5.655978957692945, 5.653984897039905, 3.390662752324637, -1.1326581026841538, -7.914648294217784,\n" + //
                            "Logarithmic\n" + //
                            "P1(x) = 49.140617215183795ln(x) + -43.13621298168807\n" + //
                            "fi = -9.074532708007908, 10.850272963648514, 24.987147565672252, 35.95255940484055, 44.91195323732867, 52.487012788180316, 59.048827839352406, 64.8367589089851,\n" + //
                            "Pirson = 0.9255689697769776\n" + //
                            "S = 752.4409314764173\n" + //
                            "S2 = 9.698201711376814\n" + //
                            "ei = -13.074532708007908, 1.8502729636485142, 8.987147565672252, 10.95255940484055, 8.911953237328667, 3.4870127881803157, -4.9511721606475945, -16.163241091014896,\n" + //
                            "Pi = -3.268633177001977, 0.20558588484983492, 0.5616967228545158, 0.43810237619362197, 0.247554256592463, 0.0711635262893942, -0.07736206501011866, -0.19954618630882587,\n" + //
                            "Exp\n" + //
                            "P1(x) = 0.41176ln(x) + 0.9357851248534588\n" + //
                            "fi = 1.7593021230959711, 2.1710606222172273, 2.5828191213384835, 2.9945776204597396, 3.406336119580996, 3.818094618702252, 4.229853117823508, 4.641611616944765,\n" + //
                            "Pirson = 0.9776634758086947\n" + //
                            "S = 0.3290967846260453\n" + //
                            "S2 = 0.2028228243523289\n" + //
                            "ei = 0.37300776197608054, -0.026163955118992277, -0.18976960090129769, -0.22429820440846093, -0.1771828188751141, -0.07372567940837449, 0.0709700344638362, 0.24716246227232563,\n" + //
                            "Pi = 0.26906822420799115, -0.011907729136505407, -0.06844491553294499, -0.06968215507898476, -0.04944380702825305, -0.018943752219023658, 0.017064686128782553, 0.05624424212748663,\n" + //
                            "Gradual\n" + //
                            "P1(x) = 2.0ln(x) + 0.0\n" + //
                            "fi = 1.3862943611198906, 2.1972245773362196, 2.772588722239781, 3.2188758248682006, 3.58351893845611, 3.8918202981106265, 4.1588830833596715, 4.394449154672439,\n" + //
                            "Pirson = 1.0\n" + //
                            "S = 0.0\n" + //
                            "S2 = 0.0\n" + //
                            "ei = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\n" + //
                            "Pi = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\n"; //
            assertEquals(result2, answer2);        
        }

        @Test
        public void testRunPythonLab3Script_Success(){
            String result1 = Lab3Test("1", "5", "-1", "1", "0.001", "4");
            String answer1 ="Infinity breaking point at 0.0\n";
            assertEquals(result1, answer1); 

            String result2 = Lab3Test("2", "4", "0", "10", "0.001", "4");
            String answer2 ="S = 333.33396911621094\n" + //
                                "Parts = 512\n" + //
                                "Innacuary = 0.0006357828776041666\n";
            assertEquals(result2, answer2); 
        }


        @Test
        public void testRunPythonLab2Script_Success(){
            String result1 = Lab2Test("false", "1", "1", "0", "1", "0.001");
            String answer1 ="x = 0.2037995283657705\n" + //
                                "y = 0.6778326100454817\n" + //
                                "Iterations = 4\n" + //
                                "inncuary x= -0.00015563740980442664\n" + //
                                "innacuary y= -4.63437782752818e-05\n";
            assertEquals(result1, answer1); 

            String result2 = Lab2Test("true", "1", "1", "0", "2", "0.001");
            String answer2 ="More than one root\n";
            assertEquals(result2, answer2); 
        }
    
}