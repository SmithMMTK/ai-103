
Microsoft Foundry มีความยืดหยุ่นสำหรับการพัฒนา generative AI chat applications ก่อนเริ่ม development สิ่งสำคัญคือการเข้าใจ options ที่มีให้เลือก และวิธีตัดสินใจว่าจะใช้แบบใด โดยประเด็นที่ควรพิจารณาในการพัฒนา application มีดังนี้:

- **Endpoints**: Microsoft Foundry projects มีสอง endpoints ที่คุณใช้เชื่อมต่อและ consume project assets จาก client applications ได้ เช่น model deployments โดยแต่ละ project จะมีทั้ง _Project endpoint_ และ _Azure OpenAI endpoint_.
- **Client SDK**: ขึ้นอยู่กับ endpoint ที่คุณเลือก คุณสามารถใช้ _Microsoft Foundry SDK_ หรือ _OpenAI SDK_ เพื่อพัฒนา generative AI chat application ได้ ทั้งสอง SDK รองรับ client object ที่เข้ากันได้กับ OpenAI API และสามารถส่ง prompts ไปยัง models ได้ แต่รายละเอียด functionality ที่มีในแต่ละ SDK จะต่างกันบางส่วน
- **Authentication**: ขึ้นอยู่กับ endpoint และ SDK ที่คุณเลือกใช้ จะมีหลายวิธีที่ client application จะถูก authenticate โดย Foundry เพื่อให้เข้าถึง assets ได้ โดยทั่วไป production applications ควรใช้ _Microsoft Entra ID_ authentication ซึ่งต้องให้ application รันในบริบทของ identity ที่ระบุชัดเจน แต่ในบางสถานการณ์ก็สามารถใช้ _key-based_ หรือ _token-based_ authentication ได้
- **Chat API**: OpenAI client API รองรับสอง chat APIs คือ _ChatCompletions_ และ _Responses_ แม้ว่า _Responses_ API จะเป็นตัวเลือกที่แนะนำสำหรับโครงการพัฒนาใหม่ส่วนใหญ่ แต่ _ChatCompletions_ API ก็เป็น API ที่ใช้งานมานานและเข้ากันได้กับ generative AI models และ platforms จำนวนมาก

มาเริ่มจากการพิจารณา endpoints, client SDKs และ authentication methods ที่มีให้เลือกก่อน แล้วเราจะไปสำรวจ Responses และ ChatCompletions APIs ในภายหลัง

## Using the Foundry SDK with the project endpoint

Microsoft Foundry SDK มอบความสามารถในการเข้าถึง resources ใน projects ของคุณแบบ programmatic ผ่าน REST API และ language-specific client libraries ซึ่งรวมถึง:

- [Azure AI Projects for Python](https://pypi.org/project/azure-ai-projects)
- [Azure AI Projects for Microsoft .NET](https://www.nuget.org/packages/Azure.AI.Projects)
- [Azure AI Projects for JavaScript](https://www.npmjs.com/package/@azure/ai-projects)

> [!NOTE]
>  
> โมดูลนี้ใช้ตัวอย่าง Python code สำหรับงานทั่วไป คุณสามารถอ้างอิงเอกสารของ language-specific SDK เพื่อดู code ที่เทียบเท่ากันในภาษาที่คุณต้องการได้ แต่ละ SDK ถูกพัฒนาและดูแลแยกจากกัน จึงอาจมีบาง functionality ที่อยู่ในระดับความพร้อมต่างกัน

### Installing the SDK

หากต้องการใช้ Azure AI Projects library ใน Python ให้ติดตั้ง package **azure-ai-projects** จาก PyPI พร้อม supporting packages ดังนี้:

Bash

```
pip install azure-ai-projects azure-identity openai
```

 Note

เมื่อใช้ Foundry SDK เพื่อพัฒนา chat application คุณต้อง import OpenAI SDK package ด้วย เนื่องจาก chat client functionality ใน Foundry SDK ต่อยอดมาจาก OpenAI SDK

### Connecting to the project endpoint

แต่ละ Foundry project มี endpoint ที่ไม่ซ้ำกัน ซึ่งคุณสามารถดูได้จากหน้า **Overview** ของ project ใน Foundry portal ที่ [https://ai.azure.com](https://ai.azure.com/)

project endpoint มีรูปแบบดังนี้:

```
https://{resource-name}.services.ai.azure.com/api/projects/<project-name>
```

ใช้ endpoint นี้เพื่อสร้าง **AIProjectClient** object:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = "https://{resource-name}.services.ai.azure.com/api/projects/<project-name>"
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)
```

> [!NOTE]
>  
>  code นี้ใช้ default Azure credentials สำหรับการ authenticate โดยหากต้องการเปิดใช้งานการ authenticate แบบนี้ คุณต้องติดตั้ง package **azure-identity** (ตามที่แสดงในคำสั่งติดตั้งก่อนหน้า)

> [!tip]
>  
> เพื่อให้เข้าถึง project ได้สำเร็จ code ต้องรันภายใต้ authenticated Azure session ตัวอย่างเช่น คุณสามารถใช้คำสั่ง Azure CLI `az login` เพื่อลงชื่อเข้าใช้ก่อนรัน code

project client (`AIProjectClient`) ช่วยให้เข้าถึง Foundry-native operations ที่ไม่มีตัวเทียบใน OpenAI ได้ โดยใช้ project client เพื่อ:

- Retrieve resource connections
- Access project configuration
- Enable tracing
- Manage datasets and indexes

### Creating a chat client

หากต้องการ chat กับ model ใน Foundry project ของคุณ คุณต้องมี OpenAI-compatible client object โดยสามารถใช้เมธอด **get_openai_client()** ของ project client เพื่อสร้างได้ดังนี้:

Python

```python
openai_client = project_client.get_openai_client(api_version="2024-10-21")
```

จากนั้นคุณสามารถใช้ chat client object นี้เพื่อส่ง prompts ไปยัง models และรับ responses กลับมา

## Using the OpenAI SDK with the Azure OpenAI endpoint

OpenAI SDK คือ official client library สำหรับเรียกใช้ OpenAI API โดยจัดการทั้ง HTTP requests, authentication, retries และ response parsing ให้พร้อมใช้งาน SDK นี้ทำงานกับ OpenAI-hosted models, Azure OpenAI deployments และ Foundry models ด้วย patterns เดียวกัน

### Installing the SDK

หากต้องการใช้ OpenAI library ใน Python ให้ติดตั้ง package **openai** จาก PyPI พร้อม supporting packages ดังนี้:

Bash

```
pip install openai azure-identity
```

 Note

จำเป็นต้องใช้ package _azure-identity_ หากคุณต้องการใช้ token-based authentication เพื่อเชื่อมต่อ endpoint ด้วย Microsoft Entra ID credentials

### Connecting to the Azure OpenAI endpoint

แต่ละ Foundry project จะมี Azure OpenAI endpoint รวมมาให้ ซึ่งคุณสามารถดูได้จากหน้า **Overview** ของ project ใน Foundry portal ที่ [https://ai.azure.com](https://ai.azure.com/)

Azure OpenAI endpoint มีรูปแบบดังนี้:

```
https://{resource-name}.openai.azure.com/openai/v1
```

สร้าง OpenAI client ด้วย endpoint และ Azure credentials ของคุณ:

```python
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

openai_client = OpenAI(  
  base_url = "https://{resource-name}.openai.azure.com/openai/v1/",  
  api_key=token_provider,
)
```

นอกจาก Microsoft Entra ID (recommended) แล้ว คุณยัง authenticate ได้ด้วย API key หรือ environment variables

**API key authentication:**

```python
import os
from openai import OpenAI

openai_client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url="https://{resource-name}.openai.azure.com/openai/v1/"
)
```

> [!important]
>  
> ควรใช้ API keys อย่างระมัดระวัง โดยจัดเก็บอย่างปลอดภัยใน Azure Key Vault และไม่ควรใส่ลงใน code โดยตรง

**Environment variables:**

หากคุณกำหนด environment variables คือ `OPENAI_BASE_URL` และ `OPENAI_API_KEY` ไว้แล้ว client จะใช้งานโดยอัตโนมัติ:


```python
from openai import OpenAI

openai_client = OpenAI()  # Uses environment variables
```

ไม่ว่าคุณจะเลือก authenticate แบบใด **OpenAI** client จะเป็นตัวจัดการ model inference operations โดยใช้สำหรับ:

- Generating responses with the Responses API
- Chat completions and image generation
- Accessing Foundry direct models (non-Azure OpenAI models)

**Using an _AzureOpenAI_ client object**

โดยทั่วไปคุณควรใช้ **OpenAI** client object เพื่อ chat กับ models ผ่าน Azure OpenAI v1 endpoint อย่างไรก็ตาม คุณยังสามารถสร้าง **AzureOpenAI** client object ได้ หากต้องการใช้ functionality จาก Azure OpenAI API เวอร์ชันเฉพาะ โดยการสร้าง **AzureOpenAI** client object จำเป็นต้องระบุ API version และ Azure endpoint ดังนี้:

```python
import os
from openai import AzureOpenAI

openai_client = AzureOpenAI(
    azure_endpoint = "https://{resource-name}.openai.azure.com"
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version="2024-10-21",
)
```

## Choosing between the Foundry SDK and OpenAI SDK

Microsoft Foundry รองรับสองแนวทางสำหรับการสร้าง AI applications ซึ่งแต่ละแนวทางมีวัตถุประสงค์ต่างกัน และการเข้าใจว่าควรใช้เมื่อใดจะช่วยให้คุณสร้าง solution ที่เหมาะสมได้

### When to use the Foundry SDK

ใช้ Foundry SDK เมื่อ application ของคุณต้องการ Foundry-specific capabilities ดังนี้:

- **Foundry Agent Service** สำหรับการสร้างและจัดการ AI agents
- **Tool invocation and approval** workflows
- **Cloud evaluations** สำหรับการทดสอบและ validate AI responses
- **Tracing and observability** สำหรับ monitoring พฤติกรรมของ application
- **Foundry direct models** (non-Azure OpenAI models ที่มีใน model catalog)
- **Project metadata, connections, and governance** features

Microsoft แนะนำให้ใช้ Foundry SDK เมื่อต้องสร้าง apps ที่มี agents, evaluations หรือ Foundry-specific features

### When to use the OpenAI SDK

ใช้ OpenAI SDK เมื่อคุณต้องการ compatibility สูงสุดกับ OpenAI API ดังนี้:

- **Full OpenAI API compatibility** สำหรับ existing code และ tooling
- **Portability** ระหว่าง OpenAI และ Azure OpenAI deployments
- **Chat Completions, Responses, and Images** APIs
- **Minimal dependency** กับ Foundry-specific concepts

OpenAI SDK เหมาะอย่างยิ่งกับ model inference workloads ที่คุณต้องการให้ existing OpenAI code ใช้งานต่อได้โดยเปลี่ยนน้อยที่สุด อย่างไรก็ตาม แนวทางนี้จะไม่ให้ Foundry-specific features เช่น agents หรือ evaluations

Microsoft Foundry ช่วยให้คุณยืดหยุ่นในการสร้าง AI applications ใช้ Foundry SDK ร่วมกับ `AIProjectClient` เมื่อคุณต้องการ project-level features เช่น agents, evaluations, tracing และ connections และใช้ OpenAI SDK เมื่อคุณต้องการ model inference ที่ตรงไปตรงมาพร้อม OpenAI compatibility สูงสุด ทั้งสอง SDK ใช้งานร่วมกับ Foundry project endpoint ของคุณได้ ดังนั้นคุณสามารถผสานการใช้งานตามความเหมาะสมใน applications ของคุณได้ และยังสามารถใช้ทั้งสอง SDK ใน application เดียวกันได้ด้วย โดยใช้ Foundry SDK สำหรับ project features และ OpenAI SDK สำหรับ model inference

---

## Next unit: Generate responses with the Responses API