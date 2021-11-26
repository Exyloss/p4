package main
import (
    "fmt"
    "strconv"
)

func main() {
    var joueur int = 1
    var input string
    var color_j string = "\033[1;31m"
    dic := [7][7]int{{0}}
    num := [7]string{"1","2","3","4","5","6","7"}
    for {
        printDic(dic)
        fmt.Print(":")
        fmt.Scanln(&input)
        input2, _ := strconv.Atoi(input)
        input2 -= 1
        if contains(num, input) && isNotFull(input2, dic) {
            dic = poserPion(input2, dic, joueur)
            if isWinning(dic) {
                printDic(dic)
                fmt.Println(color_j+"Joueur", joueur, "a gagné.")
                break
            }
        } else if input == "q" {
            break
        } else {
            continue
        }
        if joueur == 1 {
            joueur = 2
            color_j = "\033[1;33m"
        } else {
            joueur = 1
            color_j = "\033[1;31m"
        }
    }
}

func printDic(dic [7][7]int) {
    var temp string = ""
    var red string = "\033[1;31m"
    var yellow string = "\033[1;33m"
    var white string = "\033[1;97m"
    fmt.Println("\033[1;34m1 2 3 4 5 6 7")
    for i := 0; i < 7; i++ {
        for j := 0; j < 7; j++ {
            if dic[i][j] == 1 {
                temp = temp+red+"0 "
            } else if dic[i][j] == 2 {
                temp = temp+yellow+"0 "
            } else {
                temp = temp+white+"0 "
            }
        }
        fmt.Println(temp+white)
        temp = ""
    }
}

func poserPion(col int, dic [7][7]int, joueur int) [7][7]int {
    for i := 6; i >= 0; i-- {
        if dic[i][col] == 0 {
            dic[i][col] = joueur
            break
        }
    }
    return dic
}

func isNotFull(col int, dic [7][7]int) bool {
    if dic[0][col] == 0 {
        return true
    }
    return false
}

func contains(arr [7]string, str string) bool {
    for _, a := range arr {
        if a == str {
            return true
        }
    }
    return false
}

func isWinning(dic [7][7]int) bool {
    var v int = 0
    for i := 0; i < 6; i++ {
        for j := 0; j < 6; j++ {
            if dic[j][i] == dic[j+1][i] && dic[j][i] != 0 {
                v += 1
            } else {
                v = 0
            }
            if v == 3 {
                return true
                break
            }
        }
        v = 0
    }

    for i := 0; i < 6; i++ {
        v = 0
        for j := 0; j < 6; j++ {
            if dic[i][j] == dic[i+1][j] && dic[i][j] != 0 {
                v += 1
            } else {
                v = 0
            }
            if v == 3 {
                return true
            }
        }
    }

    for i := 0; i < 4; i++ {
        for j := 6; j > 2; j-- {
            v = 0
            for k := 0; k < 3; k++ {
                if dic[i+k][j-k] == dic[i+k+1][j-k-1] && dic[i+k][j-k] != 0 {
                    v += 1
                } else {
                    v = 0
                }
                if v == 3 {
                    return true
                }
            }
        }
    }

    for i := 6; i > 2; i-- {
        for j := 6; j > 2; j-- {
            v = 0
            for k := 0; k < 3; k++ {
                if dic[i-k][j-k] == dic[i-k-1][j-k-1] && dic[i-k][j-k] != 0 {
                    v += 1
                } else {
                    v = 0
                }
                if v == 3 {
                    return true
                }
            }
        }
    }
    return false
}
