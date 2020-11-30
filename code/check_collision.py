import RobotUtil as rt

reference_origin = (0,0,0)
reference_orientation = (0,0,0)
reference_dim = (3,1,2)

reference_H = rt.rpyxyz2H(reference_orientation, reference_origin)
reference_corners, reference_axes = rt.BlockDesc2Points(reference_H, reference_dim)

test_cases = [
    {'origin': (0,1,0), 'orient': (0,0,0), 'dim':(0.8, 0.8, 0.8)},
    {'origin': (1.5,-1.5,0), 'orient': (1,0,1.5), 'dim':(1, 3, 3)},
    {'origin': (0,0,-1), 'orient': (0,0,0), 'dim':(2, 3, 1)},
    {'origin': (3,0,0), 'orient': (0,0,0), 'dim':(3, 1, 1)},
    {'origin': (-1,0,-2), 'orient': (.5,0,.4), 'dim':(2, .7, 2)},
    {'origin': (1.8,.5,1.5), 'orient': (-.2,.5,0), 'dim':(1, 3, 1)},
    {'origin': (0,-1.2,.4), 'orient': (0,.785,.785), 'dim':(1, 1, 1)},
    {'origin': (-.8,0,-.5), 'orient': (0,0,.2), 'dim':(1, .5, .5)}
]

def test_fn(test, reference_corners, reference_axes):
    box_origin, box_orient, box_dim = test['origin'], test['orient'], test['dim']
    box_H = rt.rpyxyz2H(box_orient, box_origin)
    box_corners, box_axes = rt.BlockDesc2Points(box_H, box_dim)
    
    for box_corner in box_corners:
        for reference_corner in reference_corners:
            if rt.CheckBoxBoxCollision(box_corner,box_axes,reference_corner,reference_axes):
                return True
    return False

ans = ['Yes' if test_fn(test,reference_corners, reference_axes) else 'No' for test in test_cases]

print (ans)