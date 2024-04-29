package com.example.webmath.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import com.example.webmath.util.ValidateFile;
import java.io.*;

@RestController
public class PythonController {

    @GetMapping("api/run-python-script")
    public String runPythonScript(@RequestParam("lbname") String lbname, @RequestParam("type") String type,
                                  @RequestParam("quation") String quation, @RequestParam("method") String method,
                                  @RequestParam("leftBorder") String leftBorder, @RequestParam("rightBorder") String rightBorder,
                                  @RequestParam("inaccuary") String inaccuary) {
        try {
            System.out.println(lbname+" "+type+" "+quation+" "+ method+" "+leftBorder+" "+rightBorder+ " "+ inaccuary);
            String currentDir = System.getProperty("user.dir");
            String scriptPath;
            String launchCommand;
            String osName = System.getProperty("os.name").toLowerCase();
            if (osName.contains("windows")) {
                scriptPath = currentDir + "\\src\\main\\resources\\scripts\\lb2\\main.py";
                launchCommand = "python";
            } else {
                scriptPath = "/home/byrybdyk/back/lb2/main.py";
                launchCommand = "python3";
            }
            ///root/back/test.py
            // Создаем объект ProcessBuilder для запуска Python скрипта
            ProcessBuilder processBuilder = new ProcessBuilder(launchCommand, scriptPath, type, quation, method, leftBorder, rightBorder,inaccuary);
            // Запускаем процесс
            Process process = processBuilder.start();

            // Читаем вывод скрипта
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder output = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }

            // Ждем завершения процесса и получаем его код возврата
            int exitCode = process.waitFor();
            System.out.println(output.toString());
            System.out.println(scriptPath);
            // Возвращаем результат выполнения скрипта и его код возврата
            return output.toString();

        } catch (IOException | InterruptedException e) {
//            e.printStackTrace();
            System.out.println(System.getProperty("user.dir"));
            return "Error executing Python script".toString();
        }
    }

    @GetMapping("api/run-python-script_lb3")
    public String runPythonScript(@RequestParam("quation") String quation, @RequestParam("method") String method,
                                @RequestParam("leftBorder") String leftBorder, @RequestParam("rightBorder") String rightBorder,
                                @RequestParam("inaccuary") String inaccuary,@RequestParam("parts") String parts) {
        try {
            System.out.println("Get request LB_3 "+quation+" "+ method+" "+leftBorder+" "+rightBorder+ " "+ inaccuary+" "+ parts);
            String currentDir = System.getProperty("user.dir");
            String scriptPath;
            String launchCommand;
            String osName = System.getProperty("os.name").toLowerCase();
            if (osName.contains("windows")) {
                scriptPath = currentDir + "\\src\\main\\resources\\scripts\\lb3\\main.py";
                launchCommand = "python";
            } else {
                scriptPath = "/home/byrybdyk/back/lb3/main.py";
                launchCommand = "python3";
            }
            ///root/back/test.py
            // Создаем объект ProcessBuilder для запуска Python скрипта
            ProcessBuilder processBuilder = new ProcessBuilder(launchCommand, scriptPath, quation, method, leftBorder, rightBorder,inaccuary, parts);
            // Запускаем процесс
            Process process = processBuilder.start();

            // Читаем вывод скрипта
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder output = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }

            // Ждем завершения процесса и получаем его код возврата
            int exitCode = process.waitFor();
            System.out.println(output.toString());
            System.out.println(scriptPath);
            // Возвращаем результат выполнения скрипта и его код возврата
            return output.toString();

        } catch (IOException | InterruptedException e) {
//            e.printStackTrace();
            System.out.println(System.getProperty("user.dir"));
            return "Error executing Python script".toString();
        }
    }
    @GetMapping("api/run-python-script_lb4")
    public String runPythonScript(@RequestParam("pair1") String pair1,@RequestParam("pair2") String pair2, @RequestParam("pair3") String pair3, @RequestParam("pair4") String pair4,@RequestParam("pair5") String pair5, 
                                    @RequestParam("pair6") String pair6,@RequestParam("pair7") String pair7, @RequestParam("pair8") String pair8, @RequestParam("pair9") String pair9, @RequestParam("pair10") String pair10,
                                    @RequestParam("pair11") String pair11, @RequestParam("pair12") String pair12) {
        try {
            System.out.println("Get request LB_4 "+ pair1+" "+ pair2+" "+ pair3+" "+ pair4+" "+ pair5+" "+ pair6+" "+ pair7+" "+ pair8+" "+ pair9+" "+ pair10+" "+ pair11+" "+ pair12);
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
            ///root/back/test.py
            // Создаем объект ProcessBuilder для запуска Python скрипта
            ProcessBuilder processBuilder = new ProcessBuilder(launchCommand, scriptPath, pair1, pair2, pair3, pair4, pair5, pair6, pair7, pair8, pair9, pair10, pair11, pair12);
            // Запускаем процесс
            Process process = processBuilder.start();

            // Читаем вывод скрипта
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder output = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }

            // Ждем завершения процесса и получаем его код возврата
            int exitCode = process.waitFor();
            System.out.println(output.toString());
            System.out.println(scriptPath);
            // Возвращаем результат выполнения скрипта и его код возврата
            return output.toString();

        } catch (IOException | InterruptedException e) {
//            e.printStackTrace();
            System.out.println(System.getProperty("user.dir"));
            return "Error executing Python script".toString();
        }
    }
    @PostMapping("/api/send-file")
    public String handleFileUpload(@RequestParam("file") MultipartFile file) {
        if (!file.isEmpty()) {
            try {
                // Читаем содержимое файла в строку
                String fileContent = new String(file.getBytes());
                String[] lines = fileContent.split("\\n");
                // Выводим содержимое файла на сервере
                System.out.println("File context");
                for (String line : lines) {
                    System.out.println(line);
                }
                ValidateFile validator = new ValidateFile();
                boolean isValid = validator.validateFile(lines);

                if(!isValid) {
                    return "Uncorrected file.";
                }

                String currentDir = System.getProperty("user.dir");
                String scriptPath;
                String launchCommand;
                String osName = System.getProperty("os.name").toLowerCase();
                if (osName.contains("windows")) {
                    scriptPath = currentDir + "\\src\\main\\resources\\scripts\\lb2\\main.py";
                    launchCommand = "python";
                } else {
                    scriptPath = currentDir + "/back/test.py";
                    launchCommand = "python3";
                }
                ///root/back/test.py
                // Создаем объект ProcessBuilder для запуска Python скрипта
                ProcessBuilder processBuilder = new ProcessBuilder(launchCommand, scriptPath, lines[0], lines[1], lines[2], lines[3], lines[4],lines[5]);
                // Запускаем процесс
                Process process = processBuilder.start();

                // Читаем вывод скрипта
                BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                StringBuilder output = new StringBuilder();
                String line;
                while ((line = reader.readLine()) != null) {
                    output.append(line).append("\n");
                }

                // Ждем завершения процесса и получаем его код возврата
                int exitCode = process.waitFor();
                System.out.println(output.toString());
                System.out.println(scriptPath);
                // Возвращаем результат выполнения скрипта и его код возврата
                return output.toString();
            } catch (IOException e) {
                return "Ошибка при чтении файла: " + e.getMessage();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        } else {
            return "Choose the file";
        }
    }

}
//while
//    pyOut
//    if pyout != exit
//    react out
//    wait react in
//    pyIn
