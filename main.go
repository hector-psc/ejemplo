package main

import (
	"errors"
	"fmt"
	"strings"
	"unicode"
)

func main() {
	nom := "Memin Pinguin Garcia luna"

	imprimir(nom)
	minusculas(&nom)
	imprimir(nom)
	mayu := mayusculas(nom)
	imprimir(nom)
	imprimir(mayu)
	//iniciales, err := iniciales(mayusculas(nom))
	//if err != nil {
	//	panic(err)
	//}
	//imprimir(iniciales)
}

func minusculas(nombre *string) {
	*nombre = strings.ToLower(*nombre)
}
func mayusculas(nombre string) string {
	nombreEnMayusculas := strings.ToUpper(nombre)
	return nombreEnMayusculas
}
func imprimir(nombre string) {
	fmt.Println(nombre)
}

func iniciales(texto string) (string, error) {
	nombres := strings.Split(texto, " ")
	todosSonNumeros := true //variable bandera
	iniciales := make([]byte, 3)
	for _, nombre := range nombres {
		n := nombre[0]
		if unicode.IsNumber(rune(n)) {
			todosSonNumeros = false
		}
		iniciales = append(iniciales, n)
	}
	if todosSonNumeros == false {
		return "", errors.New("algun nombre empieza en numero")
	}
	return string(iniciales), nil
}
