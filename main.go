package main

import (
	"fmt"
	"net/http"
)

// 定义一个处理函数，始终返回 "Hello, World!"
func helloHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, World!")
}

func main() {
	// 将 / 路由绑定到 helloHandler
	http.HandleFunc("/", helloHandler)

	// 在 8080 端口启动 HTTP 服务器
	fmt.Println("Starting server on :8080...")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Printf("Error starting server: %v\n", err)
	}
}
