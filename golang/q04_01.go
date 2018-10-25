package main

import "fmt"

func main() {
    fmt.Println(cutBarBFS(3, 8))
    fmt.Println(cutBarBFS(3, 20))
    fmt.Println(cutBarBFS(5, 100))
    fmt.Println(cutBarBin(3, 8))
    fmt.Println(cutBarBin(3, 20))
    fmt.Println(cutBarBin(5, 100))
}
func cutBarBin(m, n int) int {
    ans := 0
    for n > 1 {
        ans++
        x := n / 2
        n -= n / 2
        for x > m {
            ans++
            x /= 2
        }
    }
    return ans
}
func cutBarBFS(m, n int) int {
    // 广度优先搜索
    a := []int{n}
    ans := 0
    for len(a) > 0 {
        for i := 0; i < m && i < len(a); i++ {
            x := a[0]
            a = a[1:]
            //这里x会被2整除，但是，x为奇数，比如5, 因切割为3和2
            y := x / 2
            if y > 1 {
                a = append(a, y)
            }
            if x-y > 1 {
                a = append(a, x-y)
            }
        }
        ans++
    }
    return ans
}
