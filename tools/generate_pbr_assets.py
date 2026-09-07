from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import numpy as np, random

ROOT=Path(__file__).resolve().parents[1]; RP=ROOT/'src/resource_pack'; B=RP/'textures/blocks'; I=RP/'textures/items'; B.mkdir(parents=True,exist_ok=True); I.mkdir(parents=True,exist_ok=True)
SEED=1337

def noise(w,h,seed,blur=2):
    r=np.random.default_rng(seed).normal(127,22,(h,w)).clip(0,255).astype('uint8')
    return np.asarray(Image.fromarray(r).filter(ImageFilter.GaussianBlur(blur)),dtype=np.float32)/255-.5

def fill_metal(im,box,base,seed,amp=26):
    x0,y0,x1,y1=box; n=noise(x1-x0,y1-y0,seed)
    arr=np.empty((y1-y0,x1-x0,3),dtype=np.float32); arr[:]=base
    arr+=n[...,None]*amp; arr+=(np.sin(np.arange(y1-y0)[:,None]*1.3)*1.5)[...,None]
    im.paste(Image.fromarray(arr.clip(0,255).astype('uint8'),'RGB'),(x0,y0))

def normals(height,strength=3.0):
    gy,gx=np.gradient(height.astype(np.float32)); nx=-gx*strength; ny=-gy*strength; nz=np.ones_like(nx)
    l=np.sqrt(nx*nx+ny*ny+nz*nz); rgb=np.stack(((nx/l*.5+.5)*255,(ny/l*.5+.5)*255,(nz/l*.5+.5)*255),2)
    return Image.fromarray(rgb.clip(0,255).astype('uint8'),'RGB')

def safe(stage,name):
    im=Image.new('RGB',(256,256),(38,42,47))
    regions=[((0,0,64,64),(42,47,53)),((64,0,128,64),(54,59,65)),((128,0,160,128),(91,96,101)),((160,0,224,64),(20,23,27)),((224,0,256,64),(108,112,115)),((64,64,128,128),(46,51,57)),((128,128,192,192),(72,77,82)),((192,64,256,256),(34,38,43)),((0,128,128,256),(31,35,40))]
    for j,(box,col) in enumerate(regions): fill_metal(im,box,col,SEED+j+stage*20)
    d=ImageDraw.Draw(im)
    for x in (6,58,70,122): d.line((x,4,x,60),fill=(24,28,33),width=1)
    for y in (7,56): d.line((4,y,60,y),fill=(73,79,86)); d.line((68,y,124,y),fill=(80,86,92))
    for px,py in ((9,10),(55,10),(9,54),(55,54),(73,10),(119,10),(73,54),(119,54)): d.ellipse((px-2,py-2,px+2,py+2),fill=(128,132,134))
    d.rectangle((162,2,222,62),outline=(9,11,13),width=2); d.line((162,34,222,34),fill=(48,52,56),width=2)
    d.ellipse((226,4,254,32),fill=(58,61,63),outline=(150,154,155),width=2); d.ellipse((233,11,247,25),fill=(28,30,31),outline=(173,176,177))
    d.rectangle((0,64,63,127),fill=(47,92,58))
    for y in range(66,126,10): d.rectangle((2,y,61,y+6),fill=(58,112,68)); d.line((28,y,32,y+6),fill=(202,181,113),width=2)
    rng=random.Random(SEED+stage)
    for _ in range(stage*13):
        x=rng.randint(74,124); y=rng.randint(5,58); ln=rng.randint(5,18); col=rng.choice(((124,128,130),(160,153,139),(95,58,42)))
        d.line((x,y,min(127,x+ln),y+rng.randint(-2,2)),fill=col,width=rng.choice((1,1,2)))
    if stage>=2: d.line((118,8,124,56),fill=(118,63,42),width=2)
    if stage>=3: d.rectangle((117,20,126,45),outline=(154,83,48),width=2)
    gray=np.asarray(im.convert('L'),dtype=np.float32)/255; gray+=noise(256,256,SEED+50+stage,.8)*.16
    mer=np.zeros((256,256,3),dtype='uint8'); mer[:]=[235,0,105]; mer[160:224,0:128]=[12,0,190]; mer[64:128,0:64]=[0,0,185]; mer[0:64,224:256]=[250,0,62]
    im.save(B/f'{name}.png'); normals(gray,2.8).save(B/f'{name}_normal.png'); Image.fromarray(mer,'RGB').save(B/f'{name}_mer.png')

def crowbar():
    im=Image.new('RGB',(64,64),(75,80,84)); fill_metal(im,(0,0,64,64),(77,82,86),SEED+90,30); d=ImageDraw.Draw(im)
    d.rectangle((16,0,31,18),fill=(41,42,42))
    for y in range(2,18,3): d.line((16,y,31,y),fill=(68,69,68))
    rng=random.Random(SEED+91)
    for _ in range(70):
        x,y=rng.randrange(64),rng.randrange(64); c=rng.choice(((107,61,38),(129,75,43),(80,51,38))); d.point((x,y),fill=c)
    h=np.asarray(im.convert('L'),dtype=np.float32)/255; mer=np.zeros((64,64,3),dtype='uint8'); mer[:]=[248,0,82]; mer[:18,16:32]=[10,0,176]
    im.save(I/'crowbar_3d.png'); normals(h,3.2).save(I/'crowbar_3d_normal.png'); Image.fromarray(mer,'RGB').save(I/'crowbar_3d_mer.png')
    s=4; icon=Image.new('RGBA',(32*s,32*s)); q=ImageDraw.Draw(icon); pts=[(9*s,28*s),(14*s,21*s),(19*s,13*s),(23*s,7*s)]
    q.line(pts,fill=(25,27,29,255),width=5*s,joint='curve'); q.line(pts,fill=(116,122,125,255),width=3*s,joint='curve'); q.arc((20*s,1*s,30*s,11*s),195,330,fill=(116,122,125,255),width=3*s); q.polygon([(6*s,28*s),(11*s,24*s),(14*s,27*s),(9*s,31*s)],fill=(122,127,129,255)); icon.resize((32,32),Image.Resampling.LANCZOS).save(I/'crowbar_icon.png')

for st,n in ((0,'vault_safe'),(1,'vault_safe_stage1'),(2,'vault_safe_stage2'),(3,'vault_safe_stage3')): safe(st,n)
crowbar(); print('Generated DLavie Heist PBR assets.')
