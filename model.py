from pydantic import BaseModel, Field


class MRect(BaseModel):
    x: int
    y: int
    width: int
    height: int


class MOffset(BaseModel):
    x: int
    y: int


class MBorder(BaseModel):
    x: int
    y: int
    z: int
    w: int


class MPivot(BaseModel):
    x: float
    y: float


class First(BaseModel):
    data_0_: int = Field(..., alias='data[0]')
    data_1_: int = Field(..., alias='data[1]')
    data_2_: int = Field(..., alias='data[2]')
    data_3_: int = Field(..., alias='data[3]')


class MRenderDataKey(BaseModel):
    first: First
    second: str


class MSpriteAtlas(BaseModel):
    m_FileID: int
    m_PathID: str


class Texture(BaseModel):
    m_FileID: int
    m_PathID: str


class AlphaTexture(BaseModel):
    m_FileID: int
    m_PathID: str


class MCenter(BaseModel):
    x: int
    y: int
    z: int


class MExtent(BaseModel):
    x: int
    y: int
    z: int


class LocalAABB(BaseModel):
    m_Center: MCenter
    m_Extent: MExtent


class MSubMesh(BaseModel):
    firstByte: int
    indexCount: int
    topology: int
    baseVertex: int
    firstVertex: int
    vertexCount: int
    localAABB: LocalAABB


class MChannel(BaseModel):
    stream: int
    offset: int
    format: int
    dimension: int


class MVertexData(BaseModel):
    m_VertexCount: int
    m_Channels: list[MChannel]


class TextureRect(BaseModel):
    x: float
    y: float
    width: float
    height: float


class TextureRectOffset(BaseModel):
    x: float
    y: float


class AtlasRectOffset(BaseModel):
    x: int
    y: int


class UvTransform(BaseModel):
    x: int
    y: int
    z: int
    w: int


class MRD(BaseModel):
    texture: Texture
    alphaTexture: AlphaTexture
    secondaryTextures: list
    m_SubMeshes: list[MSubMesh]
    m_IndexBuffer: list[int]
    m_VertexData: MVertexData
    m_Bindpose: list
    textureRect: TextureRect
    textureRectOffset: TextureRectOffset
    atlasRectOffset: AtlasRectOffset
    settingsRaw: int
    uvTransform: UvTransform
    downscaleMultiplier: int


class MPhysicsShapeItem(BaseModel):
    x: float
    y: float


class Base(BaseModel):
    m_Name: str
    m_Rect: MRect
    m_Offset: MOffset
    m_Border: MBorder
    m_PixelsToUnits: int
    m_Pivot: MPivot
    m_Extrude: int
    m_IsPolygon: bool
    m_RenderDataKey: MRenderDataKey
    m_AtlasTags: list
    m_SpriteAtlas: MSpriteAtlas
    m_RD: MRD
    m_PhysicsShape: list[list[MPhysicsShapeItem]]
    m_Bones: list


class Sprite(BaseModel):
    Base: Base


class Sprites(BaseModel):
    __root__: list[Sprite]
