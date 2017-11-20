
/* */

Select Distinct 
	s.Keyword
	#,s.SessionId
	#s.AccessDateTime,
	,s1.total_searches
	,s1.sum_LinkCtg
	,s1.sum_Link
	,c.CodeFix_count
	#,c.Product_Code
