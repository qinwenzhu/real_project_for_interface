#curl  -X POST "10.253.40.87:9200/yqdlog/_delete_by_query?pretty" -H 'Content-Type:application/json' -d '
#{
#    "query": {
#        "range": {
#            "bank_interfacelog_createTime": {
#                    "gte": "now-200d",
#                    "lte": "now",
#                    "format": "epoch_millis"
#                    }
#            }
#            }
#}'
#     echo "已清除$index 索引内200天前数据~"




echo 开始执行 新增用户+启动 5个安卓 ......
for /l %%i in (1,1,%times%) do (
	echo "platform=2&deviceno=2sfdasdasdasda1sd%%i&channel=%%i"
	curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "platform=2&deviceno=2sfdasdasdasda1sd%%i&channel=%%i" http://192.168.115.197:8091/product/%api% >>result.txt
	curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "platform=2&deviceno=2sfdasdasdasda1sd%%i" http://192.168.115.197:8091/product/%api_boot% >>result.txt
)
echo