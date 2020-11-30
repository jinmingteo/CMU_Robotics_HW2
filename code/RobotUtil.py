import numpy as np 
import math

def rpyxyz2H(rpy,xyz):
	Ht=[[1,0,0,xyz[0]],
	    [0,1,0,xyz[1]],
            [0,0,1,xyz[2]],
            [0,0,0,1]]

	Hx=[[1,0,0,0],
	    [0,math.cos(rpy[0]),-math.sin(rpy[0]),0],
            [0,math.sin(rpy[0]),math.cos(rpy[0]),0],
            [0,0,0,1]]

	Hy=[[math.cos(rpy[1]),0,math.sin(rpy[1]),0],
            [0,1,0,0],
            [-math.sin(rpy[1]),0,math.cos(rpy[1]),0],
            [0,0,0,1]]

	Hz=[[math.cos(rpy[2]),-math.sin(rpy[2]),0,0],
            [math.sin(rpy[2]),math.cos(rpy[2]),0,0],
            [0,0,1,0],
            [0,0,0,1]]

	H=np.matmul(np.matmul(np.matmul(Ht,Hx),Hy),Hz)
	
	return H

def R2axisang(R):
	ang = math.acos(( R[0,0] + R[1,1] + R[2,2] - 1)/2)
	Z = np.linalg.norm([R[2,1] - R[1,2], R[0,2] - R[2,0], R[1,0] - R[0,1]])
	x = (R[2,1] - R[1,2])/Z
	y = (R[0,2] - R[2,0])/Z
	z = (R[1,0] - R[0,1])/Z 	

	return[x, y, z], ang


def BlockDesc2Points(H, Dim):
	center = H[0:3,3]
	axes=[ H[0:3,0],H[0:3,1],H[0:3,2]]	

	corners=[
		center,
		center+(axes[0]*Dim[0]/2.)+(axes[1]*Dim[1]/2.)+(axes[2]*Dim[2]/2.),
		center+(axes[0]*Dim[0]/2.)+(axes[1]*Dim[1]/2.)-(axes[2]*Dim[2]/2.),
		center+(axes[0]*Dim[0]/2.)-(axes[1]*Dim[1]/2.)+(axes[2]*Dim[2]/2.),
		center+(axes[0]*Dim[0]/2.)-(axes[1]*Dim[1]/2.)-(axes[2]*Dim[2]/2.),
		center-(axes[0]*Dim[0]/2.)+(axes[1]*Dim[1]/2.)+(axes[2]*Dim[2]/2.),
		center-(axes[0]*Dim[0]/2.)+(axes[1]*Dim[1]/2.)-(axes[2]*Dim[2]/2.),
		center-(axes[0]*Dim[0]/2.)-(axes[1]*Dim[1]/2.)+(axes[2]*Dim[2]/2.),
		center-(axes[0]*Dim[0]/2.)-(axes[1]*Dim[1]/2.)-(axes[2]*Dim[2]/2.)
		]	
	# returns corners of BB and axes
	return corners, axes



def CheckPointOverlap(pointsA,pointsB,axis):
	# check if points are overlapping
	# project points
	proj_points_A = np.matmul(axis, np.transpose(pointsA))
	proj_points_B = np.matmul(axis, np.transpose(pointsB))

	# Check overlap
	maxA , minA = np.max(proj_points_A), np.min(proj_points_A)
	maxB , minB = np.max(proj_points_B), np.min(proj_points_B)

	if maxA <= maxB and maxA >= minB:
		return True
	
	elif maxB <= maxA and maxB >= minA:
		return True
	
	elif minA <= maxB and minA >= minB:
		return True

	elif minB <= maxA and minB >= minA:
		return True 

	return False


def CheckBoxBoxCollision(pointsA,axesA,pointsB,axesB):
	# check collision between two boxes

	# sphere check 
	if np.linalg.norm(pointsA[0] - pointsB[0]) > np.linalg.norm(pointsA[0] - pointsA[1]) + np.linalg.norm(pointsB[0] - pointsB[1]):
		return False
	
	# surface normal check
	for i in range(3):
		if not CheckPointOverlap(pointsA=pointsA, pointsB=pointsB, axis=axesA[i]):
			return False
		if not CheckPointOverlap(pointsA=pointsA, pointsB=pointsB, axis=axesB[i]):
			return False
	
	# edge to edge check
	for i in range(3):
		for j in range(3):
			if not CheckPointOverlap(pointsA=pointsA, pointsB=pointsB, axis=np.cross(axesA[i], axesB[j])):
				return False
	
	return True

	