package main

import (
    "fmt"
    "os"
    "errors"
)

func checkErr(err error) {
    if err != nil {
        panic(err)
    }
}

func generateInputsFile(path string) {
    // check if file exists
    _, err := os.Stat(path)
    if err == nil {
        fmt.Printf("File %s already exists.\nExiting NOW\n", path)
        os.Exit(0)
    } else if errors.Is(err, os.ErrNotExist) {
        file, err := os.Create(path)
        checkErr(err)

        defer file.Close()

        var bytes int = 0
        for i := 1; i < 101; i++ {
            line := fmt.Sprintf("This is line number %d\n", i)
            sum, err := file.WriteString(line)
            checkErr(err)
            bytes += sum
        }

        file.Sync()
        fmt.Printf("Wrote %d bytes in %s\n", bytes, path)
    } else {
        fmt.Printf("Error: %s", err)
        fmt.Println("Some weird shit happened, exiting NOW")
        os.Exit(1)
    }
}

func main() {
    var inputs string = "/tmp/inputs.log"
    generateInputsFile(inputs)
}
