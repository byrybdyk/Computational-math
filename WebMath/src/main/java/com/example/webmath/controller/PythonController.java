package com.example.webmath.controller;

import org.apache.coyote.Request;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

@RestController
public class PythonController {

    @GetMapping("api/run-python-script")
    public String runPythonScript(@RequestParam("lbname") String lbname, @RequestParam("type") String type,
                                  @RequestParam("quation") String quation, @RequestParam("method") String method,
                                  @RequestParam("leftBorder") String leftBorder, @RequestParam("rightBorder") String rightBorder) {
        try {
            System.out.println(lbname+" "+type+" "+quation+" "+ method+" "+leftBorder+" "+rightBorder);
            String currentDir = System.getProperty("user.dir");
            String scriptPath;
            String launchCommand;
            String osName = System.getProperty("os.name").toLowerCase();
            if (osName.contains("windows")) {
                scriptPath = currentDir + "\\src\\main\\resources\\scripts\\test.py";
                launchCommand = "python";
            } else {
                scriptPath = currentDir + "/back/test.py";
                launchCommand = "python3";
            }
            ///root/back/test.py
            // Создаем объект ProcessBuilder для запуска Python скрипта
            ProcessBuilder processBuilder = new ProcessBuilder(launchCommand, scriptPath,leftBorder,rightBorder);
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
}
//while
//    pyOut
//    if pyout != exit
//    react out
//    wait react in
//    pyIn
