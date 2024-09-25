/*   Problem statement:  */
//
//     Implement compress() and decompress() functions
//   for a basic string compression/decompression scheme.
//   In particular, we would like to compress strings with
//   long runs of the same character.
//
//   For example:
//   - compress "aaabbbbbbccddddaa" into "a3b6c2d4a2".
//   - decompress "a3b6c2d4a2" into "aaabbbbbbccddddaa".
package main

import "fmt"

func main() {
	input := inputs()
	compressed := compress(input)
	fmt.Println(compressed)
	// decompressed := decompress(input)
	// fmt.Println(decompressed)
}

func compress(input string) string {
	result := ""
	return result + input
}

func decompress(input string) string {
	result := ""
	return result + input
}
