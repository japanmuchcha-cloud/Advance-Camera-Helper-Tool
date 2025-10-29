import maya.cmds as cmds
import random

# ---------------- CREATE CAMERA ----------------
def create_camera(name="Camera1", focal_length=35):
    if cmds.objExists(name):
        cmds.warning(f"Camera {name} already exists.")
        return name
    cam_transform, cam_shape = cmds.camera()
    cam_transform = cmds.rename(cam_transform, name)
    cam_shape = cmds.listRelatives(cam_transform, shapes=True)[0]
    new_shape = cmds.rename(cam_shape, f"{name}Shape")
    cmds.setAttr(f"{new_shape}.focalLength", focal_length)
    return cam_transform

# ---------------- REALTIME MOVE ----------------
def set_camera_transform(camera, translate, rotate):
    if camera and cmds.objExists(camera):
        cmds.xform(camera, translation=[translate['X'], translate['Y'], translate['Z']], worldSpace=True)
        cmds.xform(camera, rotation=[rotate['X'], rotate['Y'], rotate['Z']], worldSpace=True)
        cmds.refresh()

# ---------------- SET KEYFRAME ----------------
def set_keyframe(camera):
    if camera and cmds.objExists(camera):
        cmds.setKeyframe(camera, attribute='translate')
        cmds.setKeyframe(camera, attribute='rotate')
        for attr in ['translateX','translateY','translateZ','rotateX','rotateY','rotateZ']:
            cmds.keyTangent(camera, attribute=attr, itt='auto', ott='auto')

# ---------------- CAMERA SHAKE ----------------
def camera_shake(camera, intensity=0.3, start_frame=1, end_frame=24, step=10):
    """
    สร้าง Camera Shake แบบ handheld
    - intensity : ความแรงของการสั่น
    - start_frame : frame เริ่ม
    - end_frame : frame สิ้นสุด
    - step : เว้นระยะ keyframe (ทุก n frames)
    """
    if not camera or not cmds.objExists(camera):
        cmds.warning("No valid camera selected.")
        return

    # เก็บค่าการหมุนเดิม
    base_rx = cmds.getAttr(f"{camera}.rotateX")
    base_ry = cmds.getAttr(f"{camera}.rotateY")
    base_rz = cmds.getAttr(f"{camera}.rotateZ")

    for f in range(start_frame, end_frame + 1, step):
        cmds.currentTime(f)
        noise_x = random.uniform(-intensity, intensity)
        noise_y = random.uniform(-intensity, intensity)
        noise_z = random.uniform(-intensity, intensity)

        cmds.setAttr(f"{camera}.rotateX", base_rx + noise_x)
        cmds.setAttr(f"{camera}.rotateY", base_ry + noise_y)
        cmds.setAttr(f"{camera}.rotateZ", base_rz + noise_z)

        cmds.setKeyframe(camera, attribute='rotateX')
        cmds.setKeyframe(camera, attribute='rotateY')
        cmds.setKeyframe(camera, attribute='rotateZ')

    # ให้ curve smooth
    for attr in ['rotateX','rotateY','rotateZ']:
        cmds.keyTangent(camera, attribute=attr, itt='spline', ott='spline')

    cmds.inViewMessage(amg='<hl>Camera Shake applied</hl>', pos='midCenter', fade=True)

