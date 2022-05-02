# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from bs4 import BeautifulSoup
import urllib3
import requests
class ProductTemplate(models.Model):
	_inherit = 'product.template'
	
	url_product = fields.Char(string="Publishing product")
	url_audio = fields.Char(string="Down load Audio link")
	url_lab = fields.Char(string="Image Link")
	content = fields.Text(string="Content")
	url_publishing = fields.Char(string="Url Publishing")
	publishing = fields.Char(string="Publishing")
	publishing_company = fields.Char(string="Company")
	sku_number = fields.Integer(string="sku_number")
	original_price = fields.Float(string="Original price")
	state_out_of_stock = fields.Char(string="state Publishing")
	out_of_stock_publishing = fields.Boolean (string="out of stock Publishing")
	dimension = fields.Char(string="Dimension")
	inf_page = fields.Char(string="Trang")
	product_line = fields.One2many('product.product', 'product_tmpl_id' ,'Product Line' )
	def _update_inf_product(self, url_publishing):
		self.ensure_one()
		if not self or not url_publishing or self == url_publishing:
			return url_publishing
		content ='test'
		
		return content

	def _update_inf_product_kimdong(self, url_publishing):
		self.ensure_one()
		if not self or not url_publishing or self == url_publishing:
			return url_publishing
		url = self.url_product
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser")
		sku_number_kd_item = soup.find_all(class_='field-items')
		
		sku_number_kd = BeautifulSoup(str(sku_number_kd_item[0]), 'html.parser')
		if sku_number_kd.find('span'):
			sku_number = int(sku_number_kd.find('span').text)
			self.write({'barcode': sku_number})
		else:
			sku_number = int(sku_number_kd.find('div').text)
		#self.write({'barcode': sku_number})
		#content
		content_kimdong_item = soup.find_all(class_='pro-tabcontent')
		content_kimdong = BeautifulSoup(str(content_kimdong_item[0]), 'html.parser')
		content_kd = str(content_kimdong.find('div').text)
		content = content_kd.lstrip(' ')
		
		#<div data-id="1038641116" data-title="Tập tục quê em - Cúng Rằm" id="combo-program"></div>
		name_product = soup.title.string
		#self.write({'name': name_product})
		#<span class="rsp-original-price"><s>30,000₫</s></span>
		if soup.find_all(class_='original-price ComparePrice'):
			original_price_kimdong_item = soup.find_all(class_='original-price ComparePrice')[0]
			original_price_kimdong = BeautifulSoup(str(original_price_kimdong_item), 'html.parser')
			original_price = int(original_price_kimdong.find('s').text[:-5]) * 1000
		else:
			original_price_kimdong_item = soup.find_all(class_='rsp-original-price')[0]
			original_price_kimdong = BeautifulSoup(str(original_price_kimdong_item), 'html.parser')
			original_price=int(original_price_kimdong.find('s').text[:-5])*1000
		if len(soup.find_all(class_='btnOutOfStock'))>0:
			out_of_stock_publishing = False
		else:
			out_of_stock_publishing = True
		self.write({'original_price': original_price,'list_price':original_price,'out_of_stock_publishing':out_of_stock_publishing,'content':content,'name':name_product})
		 
		#infpage = soup.find_all(
		#	class_='field field-name-field-product-sotrang field-type-number-decimal field-label-inline clearfix')
		# num_page= infpage.find_all(data-title_='field-item even')
		#import pdb
		#pdb.set_trace()
		#import pdb
		#pdb.set_trace()
		
		return True
	def _update_inf_product_adcbook(self, url_publishing):
		self.ensure_one()
		if not self or not url_publishing or self == url_publishing:
			return url_publishing
		url = self.url_product
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser")
		sku_number_item = soup.find_all(class_='chi_tiet')
		inf_product = BeautifulSoup(str(sku_number_item[0]), 'html.parser')
		
		if len(inf_product.find_all('td')[1]):
			barcode = inf_product.find_all('td')[1].text
			self.write({'barcode': barcode})
		else:
			barcode= ''
		
		# else:
		# 	sku_number_la = int(inf_product.find_all('td')[2].text)
		# 	self.write({'barcode': sku_number_la})
		if inf_product.find_all('td')[7]:
			if (inf_product.find_all('td')[7].text[-1])=='g':
				weight_la =	float(inf_product.find_all('td')[7].text[:-1])*0.001
			else:
				weight_la = float(inf_product.find_all('td')[7].text)*0.001
			
		if inf_product.find_all('td')[3]:
			publishing_company = inf_product.find_all('td')[3].text
			self.write({'publishing_company': publishing_company})
		if inf_product.find_all('td')[5]:
			publishing = inf_product.find_all('td')[5].text
			self.write({'publishing': publishing})
		#self.write({'barcode': sku_number_la})
		#content
		content_item = soup.find_all(class_='gioi_thieu_sach')

		content = BeautifulSoup(str(content_item[0]), 'html.parser')
		content_la = str(content.find('p').text)
		
		#<div data-id="1038641116" data-title="Tập tục quê em - Cúng Rằm" id="combo-program"></div>
		name_product = soup.find_all(class_='title')[0]
		get_product_name = BeautifulSoup(str(name_product), 'html.parser')
		name_product_la = str(get_product_name.find('div').text)
		#self.write({'name': content_la})
		#<span class="rsp-original-price"><s>30,000₫</s></span>
		if inf_product.find_all('td')[9]:
			dimension = inf_product.find_all('td')[9].text
			self.write({'dimension': dimension})
		if inf_product.find_all('td')[13]:
			inf_page = inf_product.find_all('td')[13].text
			self.write({'inf_page': inf_page})
		if soup.find_all(class_='old_price'):
			original_price_item = soup.find_all(class_='old_price')[0]
			original_price = BeautifulSoup(str(original_price_item), 'html.parser')
			original_price_la = int(original_price.find('span').text[:-6]) * 1000
		else:
			original_price_kimdong_item = soup.find_all(class_='rsp-original-price')[0]
			original_price_kimdong = BeautifulSoup(str(original_price_kimdong_item), 'html.parser')
			original_price=int(original_price_kimdong.find('s').text[:-5])*1000
		if len(soup.find_all(class_='btnOutOfStock'))>0:
			out_of_stock_publishing = False
		else:
			out_of_stock_publishing = True
		self.write({'weight': weight_la,'original_price': original_price_la,'list_price':original_price_la,'out_of_stock_publishing':out_of_stock_publishing,'content':content_la,'name':name_product_la})
		 
		#infpage = soup.find_all(
		#	class_='field field-name-field-product-sotrang field-type-number-decimal field-label-inline clearfix')
		# num_page= infpage.find_all(data-title_='field-item even')
		#import pdb
		#pdb.set_trace()
		#import pdb
		#pdb.set_trace()
		return True
	def button_update_inf_product(self):
		if self.url_publishing == 'https://nxbkimdong.com.vn':
			inf_prodcut = self._update_inf_product_kimdong(self.url_publishing)
		elif self.url_publishing == 'http://adcbookiz.vn':
			inf_prodcut = self._update_inf_product_adcbook(self.url_publishing)

		return True
	
	