# Copyright (c) 2024, abc and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class LibraryMember(Document):
	pass


@frappe.whitelist()
def get_author_articles(author):
	print("------------------------------------------",author)
	articles = frappe.db.sql(""" SELECT * FROM `tabArticle Library` WHERE article_author = {author} """, as_dict=True)
	print("article",articles)
	return articles
	