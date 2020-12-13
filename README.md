## Q2

```
python check_collision.py
```

Output: 

```
['No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes']
```

## Q3

### PRM Planner Outline

The PRM planner uses 2500 num_samples, resulting in about 7 points (inclusive of qInit and qGoal). These points are then broken into 10 smaller steps using linear interpolation. 

### Time History Plot for Joints (ang)
![Plot](https://github.com/jinmingteo/CMU_Robotics_HW2/blob/master/demo/joint_angle_vs_dt.jpeg)

### LoCoBot Video
![Video](https://github.com/jinmingteo/CMU_Robotics_HW2/blob/master/demo/interpolate_steps_10.gif)

