
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import com.example.webmath.controller.PythonController;
public class PythonControllerTest {
    private final PythonController pythonController = new PythonController();

    @Test
    public void testRunPythonScript_Success() {
        String result ="aasdasdasdf";
        String pair1 = "2 2", pair2 = "3 3", pair3 = "4 4", pair4 = "5 5", pair5 = "6 6", pair6 = "7 7", pair7 = "8 8", pair8 = "9 9",pair9="", pair10 = "", pair11 = "", pair12 = "";
        String answer ="P1(x) = 1.0x + 0.0zzP1(x) = 0x^2 + 1x + 0zzP1(x) = 0.00020879882498145205x^3 + 0.12766556727437353x^2 + -0.4252011225162542x + 3.25365243287883zzP1(x) = 4.642652787836518ln(x) + -1.9293050049752978zzP1(x) = 0.20588ln(x) + 0.4678925624267294zzP1(x) = 1.0ln(x) + 0.0zzspace\r\n" + //
                        "Best quation is P1(x) = 1.0x + 0.0 with S2 = 0.0\r\n" + //
                        "Linear\r\n" + //
                        "P1(x) = 1.0x + 0.0\r\n" + //
                        "fi = 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0,\r\n" + //
                        "Pirson = 1.0\r\n" + //
                        "S = 0.0\r\n" + //
                        "S2 = 0.0\r\n" + //
                        "ei = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\r\n" + //
                        "Pi = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\r\n" + //
                        "Quadratic\r\n" + //
                        "P1(x) = 0x^2 + 1x + 0\r\n" + //
                        "fi = 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0,\r\n" + //
                        "\r\n" + //
                        "S = 0.0\r\n" + //
                        "S2 = 0.0\r\n" + //
                        "ei = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\r\n" + //
                        "Pi = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\r\n" + //
                        "Qubic\r\n" + //
                        "P1(x) = 0.00020879882498145205x^3 + 0.12766556727437353x^2 + -0.4252011225162542x + 3.25365243287883\r\n" + //
                        "fi = 2.915582847543667, 3.1326767390739283, 3.6088601440026027, 4.345385855279578, 5.343506665854746, 6.604475368677991, 8.129544756699206, 9.919967622868276,\r\n" + //
                        "S = 2.8879506360989007\r\n" + //
                        "S2 = 0.6008276204639419\r\n" + //
                        "ei = 0.9155828475436669, 0.1326767390739283, -0.3911398559973973, -0.6546141447204219, -0.6564933341452539, -0.3955246313220089, 0.12954475669920562, 0.9199676228682758,\r\n" + //
                        "Logarithmic\r\n" + //
                        "P1(x) = 4.642652787836518ln(x) + -1.9293050049752978\r\n" + //
                        "fi = 1.2887366852323545, 3.1711703997611593, 4.506778375440007, 5.542756406036664, 6.389212089968812, 7.104880173415726, 7.724820065647657, 8.271645804497616,\r\n" + //
                        "Pirson = 0.9776634758086947\r\n" + //
                        "S = 1.8553133789257892\r\n" + //
                        "S2 = 0.4815746799466555\r\n" + //
                        "ei = -0.7112633147676455, 0.17117039976115933, 0.5067783754400068, 0.5427564060366636, 0.3892120899688116, 0.10488017341572586, -0.27517993435234267, -0.7283541955023836,\r\n" + //
                        "Pi = -0.35563165738382274, 0.057056799920386446, 0.1266945938600017, 0.10855128120733273, 0.0648686816614686, 0.014982881916532267, -0.034397491794042834, -0.08092824394470928,\r\n" + //
                        "Exp\r\n" + //
                        "P1(x) = 0.20588ln(x) + 0.4678925624267294\r\n" + //
                        "fi = 0.8796510615479856, 1.0855303111086136, 1.2914095606692417, 1.4972888102298698, 1.703168059790498, 1.909047309351126, 2.114926558911754, 2.3208058084723824,\r\n" + //
                        "Pirson = 0.9776634758086947\r\n" + //
                        "S = 0.08227419615651133\r\n" + //
                        "S2 = 0.10141141217616445\r\n" + //
                        "ei = 0.18650388098804027, -0.013081977559496138, -0.09488480045064884, -0.11214910220423047, -0.08859140943755706, -0.036862839704187245, 0.0354850172319181, 0.12358123113616282,\r\n" + //
                        "Pi = 0.26906822420799115, -0.011907729136505407, -0.06844491553294499, -0.06968215507898476, -0.04944380702825305, -0.018943752219023658, 0.017064686128782553, 0.05624424212748663,\r\n" + //
                        "Gradual\r\n" + //
                        "P1(x) = 1.0ln(x) + 0.0\r\n" + //
                        "fi = 0.6931471805599453, 1.0986122886681098, 1.3862943611198906, 1.6094379124341003, 1.791759469228055, 1.9459101490553132, 2.0794415416798357, 2.1972245773362196,\r\n" + //
                        "Pirson = 1.0\r\n" + //
                        "S = 0.0\r\n" + //
                        "S2 = 0.0\r\n" + //
                        "ei = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,\r\n" + //
                        "Pi = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,";
        try {
            String currentDir = System.getProperty("user.dir");
            String scriptPath;
            String launchCommand;
            String osName = System.getProperty("os.name").toLowerCase();
            if (osName.contains("windows")) {
                scriptPath = currentDir + "\\src\\main\\resources\\scripts\\lb4\\main.py";
                launchCommand = "python";
            } else {
                scriptPath = "/home/byrybdyk/back/lb4/main.py";
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
            int exitCode = process.waitFor();
        }catch (IOException | InterruptedException e) {
        }
    
        
        
        assertEquals(result, answer);
    }
    @Test
    public void testTest(){
        Boolean result = false;
        assertFalse(result);
    }

    
}