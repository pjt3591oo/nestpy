# NestPy

해당 프로젝트는 패키지, 라이브러리 제작시 구조를 잡아주는 패키지입니다.

NestPy의 전략은 다음과 같습니다.

NestPy를 사용한 프로젝트는 비즈니스 로직을 담당하는 **`Service`**와 로직들을 제어하는 **`Controller`**로 구성되며, 이 둘을 **`Module`**로 묶어 패키징화 합니다. 

**`Module`** 별로 의존성을 낮추기 위해 **`DI`** 패턴과 객체의 효율성을 위해 **`Singleton`**을 사용합니다.

**`Module`**, **`Controller`**, **`Service는`** **`@`**(**`데코레이터`**) 표현식으로 구성합니다.

## Module

```py
from nestpy.common.Module import Module
@Module({
  "imports": [],
  "providers": [{
    "name": "AppService",
    "provider": AppService
  }],
  "exports": [],
  "controllers": []
})
class AppModule :
  def __init__(self):
    pass
```

## Controller

## Service

```py
from nestpy.common import Injectable

@Injectable그러
class UserService:
  
  def __init__(self):
    pass
```