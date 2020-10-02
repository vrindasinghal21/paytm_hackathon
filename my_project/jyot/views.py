from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
import json
from .models import *

def Signup(request):
	print("hi")
	if request.method == 'POST':
		print(request.body)
		info=json.loads(request.body)
		pwd = info['password']
		password = pwd[::-1]
		check=Signin.objects.filter(username=info['username']).values('name')
		if check:
			return JsonResponse({"message": "Username already taken"},status=200)
		else:
			query = Signin.objects.create(name=info['name'],mobile=info['mobile'], password=password,username= info['username'],email=info['email'])
			if query:
	
				return JsonResponse({"message": "Successfully registered"},status=200)

	else:
		return JsonResponse({"message":"Could not submit"},status=502)

def login(request):

	data_values={}
	if request.method == 'POST':
	  	info =json.loads(request.body.decode("utf-8"))
	  	pwd = info['password']
	  	password = pwd[::-1]
	  	query=Signin.objects.filter(username=info['username'],password=password).values('uniq_id')
	  	if list(query):
	  		data_values={'message':"Success",'uniq_id':query[0]['uniq_id']}
	  		return JsonResponse(data=data_values,status=200,safe=False)
	  	else:
	  		return  JsonResponse({"message":"invalid credentials"},status=200)

	else:
		return JsonResponse({"message":"Error"},status=502)

def user_data(request):
	if request.method == 'POST':
		info =json.loads(request.body.decode("utf-8"))
		query = Materials.objects.create(sub_category=info['sub_category'],category=info['category'],added_by=Signin.objects.get(uniq_id=info['uniq_id']),authsize=info['authsize'],quantity=info['quantity'],standardsize=info['standardsize'],material=Dropdown.objects.get(uniq_id=info['m_id']))
		if (query):
			print(query)
			return JsonResponse({"message":"Successfully added"},status=200)

		else:
			return  JsonResponse({"message":"Error adding question"},status=200)
	elif request.method == "GET":
		if request.GET['request_type'] == 'login_id':
			username=request.GET['username']
			password=request.GET['password']
			query=Signin.objects.filter(username=info['username'],password=password).values('uniq_id')
			if list(query):
				data_values={'message':"Success",'uniq_id':query[0]['uniq_id']}
				return JsonResponse(data=data_values,status=200,safe=False)
			else:
				return  JsonResponse({"message":"invalid credentials"},status=200)
		elif request.GET['request_type'] == "form_data":
			uid = request.GET['uniq_id']
			query = Request.objects.filter(user_id_added_by_uniq_id=uid,approval_status="PENDING").values('govt_id__name','govt_id__username','govt_id__email','govt_id__mobile','required')
			return JsonResponse(data=list(query),status=200,safe=True)
		elif request.GET['request_type'] == "material":
			query = Dropdown.objects.filter(field="MATERIALS").values('value','uniq_id')
			return JsonResponse(data=list(query),status=200,safe=False)
		elif request.GET['request_type'] == "accept_reject":
			user_id = request.GET['user_id']
			id=request.GET['id']###here id is the govt id
			if id==-1:
				qry = Request.objects.filter(user_id_added_by_uniq_id=user_id,approval_status="PENDING").values_list('auto_id',flat=True)
				Request.objects.filter(auto_id__in=qry).update(approval_status="REJECTED")
			else:
				quantity1 = Request.objects.filter(user_id_added_by_uniq_id=user_id,govt_id=id).values_list('required',flat=True)
				quantity2 = Materials.objects.filter(added_by__name='user',added_by__uniq_id=user_id,status='INSERT').values_list('quantity',flat=True)
				if quantity1==quantity2:
					Request.objects.filter(user_id_added_by_uniq_id=user_id,govt_id=id).update(approval_status="APPROVED",user_id_added_by_uniq_id__status="DELETE")
				else:
					quan=quantity2-quantity1
					Materials.objects.filter(added_by__name='user',status='INSERT',added_by__uniq_id=user_id).update(quantity=quan)
	else:
		return JsonResponse({"message":"Error"},status=502)

def govt_data(request):
	if request.method == "POST":
		info = json.loads(request.body)
		query = Materials.objects.create(sub_category=info['sub_category'],category=info['category'],added_by=Signin.objects.get(uniq_id=info['uniq_id']),authsize=info['authsize'],quantity=info['quantity'],standardsize=info['standardsize'],material=Dropdown.objects.get(uniq_id=info['m_id']))
		return JsonResponse({"message":"Successfully Inserted"},status=200)
	elif request.method == "GET":
		if request.GET['request_type'] == "view":
			id= request.GET['uniq_id']
			query1 = Materials.objects.filter(added_by=id,added_by__name='school',status='INSERT').values('added_by','material','category','sub_category','authsize','quantity','standardsize')
			query2 = Materials.objects.filter(added_by__name='user',status='INSERT',material=query[0]['material'],category=query[0]['category'],sub_category=query1[0]['sub_category'],authsize=query1[0]['authsize'],standardsize=query1[0]['standardsize']).values('added_by','material','category','sub_category','authsize','quantity','standardsize')
			if query2:
				for q in query2:

					if q['quantity']>=query1[0]['quantity']:
						quan=query[0]['quantity']
						Request.objects.create(user_id_added_by_uniq_id=Materials.objects.get(auto_id=data[0]['auto_id']),govt_id=Signin.objects.get(uniq_id=info['uniq_id']),required=quan)
					else:
						quan=info['quantity']-data[0]['quantity']
						Request.objects.create(user_id_added_by_uniq_id=Materials.objects.get(auto_id=data[0]['auto_id']),govt_id=Signin.objects.get(uniq_id=request.GET['uniq_id']),required=request.GET['quantity'])
				return JsonResponse({"message":"Successfully Request Is Sent To User"},status=200)	
			else:
				return JsonResponse({"message":"Successfully Inserted"},status=200)
	else:
		return JsonResponse({"message":"Error"},status=502)
