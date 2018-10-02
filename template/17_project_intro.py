介绍的顺序和关键词：
the project intro
PRD(BA给的jira和我optimized以后的结果)
UI illutration(static/ dynamic) 画UI的图
Architecture(top-down)：按照发生的时间先后的顺序，熟悉每个component的功能
DB design: schema
Evolve:
需要改进的空间，比如root cause变成动态的，加permission management.


component介绍：
firehose:
	amazon kinesis data firehose is part of kinesis streaming data platform
elastic search:
	is a search engine based on Lucene
	用的query DSL语言，not SQL
	a JSON-style domain-specific language
	https://www.elastic.co/guide/en/elasticsearch/reference/current/_introducing_the_query_language.html
kibana:
	is an open source data visualization plugin for Elasticsearch.

data schema部分：
分成 meta data 和specific data:
meta data:
 author
 version
 created_time
 trace_id (A trace id represents one particular trace for one request)

specific data:
 event_type: "root cause"
 content: "vehicle out of range"
 comment:"I think XXXX"

ES: 存的record多，只加不减，但是读取慢
redshift: 读取快， memory
cloudwatch： 存loggin，disk，只写不读

