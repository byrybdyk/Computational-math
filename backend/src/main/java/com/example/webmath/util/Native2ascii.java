package com.example.webmath.util;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


public class Native2ascii {
    public List<String> read() {
        String filePath = "src/main/resources/badText.conf";
        List<String> lines = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            // Читаем файл построчно и добавляем каждую строку в список
            while ((line = reader.readLine()) != null) {
                lines.add(line);
            }
        } catch (IOException e) {
            lines.add("Error: " + e.getMessage());
            return lines;
        }
        return lines;
    }
}
