package com.example.webmath.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

@RestController
public class PythonController {

    @GetMapping("/run-python-script")
    public String runPythonScript(@RequestParam("argument1") String argument1, @RequestParam("argument2") String argument2) {
        try {
            String currentDir = System.getProperty("user.dir");
            String scriptPath = currentDir + "\\WebMath\\src\\main\\resources\\scripts\\test.py";

            // Создаем объект ProcessBuilder для запуска Python скрипта
            ProcessBuilder processBuilder = new ProcessBuilder("python", scriptPath, argument1,argument2);
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

//            System.out.println("Текущее расположение в корневой системе: " + currentDir+scriptPath);
            // Возвращаем результат выполнения скрипта и его код возврата
            return "Python script executed with output:\n" + output.toString();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();

            return "Error executing Python script: " + e.getMessage();
        }
    }
}
//while
//    pyOut
//    if pyout != exit
//    react out
//    wait react in
//    pyIn
