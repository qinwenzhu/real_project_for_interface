#!/usr/bin/env bash

echo 开始执行 新增用户+启动 5个安卓 ......
for /l%%i in () do (
	echo "platform=2&deviceno=2sfdasdasdasda1sd%%i&channel=%%i"
	curl -X DELETE -d "platform=struct-history-2020-05-14" http://10.151.3.97:30908/struct-history-2020-05-14
	curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "platform=2&deviceno=2sfdasdasdasda1sd%%i" http://192.168.115.197:8091/product/%api_boot% >>result.txt
)
echo

# curl -X DELETE http://10.151.3.97:30908/struct-history-2020-05-14