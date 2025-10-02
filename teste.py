import requests
import os
email="""Subject: Proposal of Potential Initiatives for Team Enhancement  Dear [Boss's Name],  I hope this email finds you well.  I have been giving some thought to potential initiatives that could benefit our team and would like to share a brief outline for your consideration.  Potentially Useful Ideas:      Cross-Training Program: Implementing a program where team members can shadow and learn key functions from other roles. This could enhance operational resilience, foster a more collaborative environment, and provide valuable professional development opportunities for the team.      Streamlined Project Kick-off Template: Creating a standardized checklist and template for launching new projects. This could help ensure all necessary resources, stakeholders, and success metrics are identified from the outset, potentially improving project efficiency and clarity.      Centralized "Ideas Hub": Establishing a simple, shared digital space (e.g., a Teams channel or shared document) where employees can freely post and discuss suggestions for improvement. This could help capture innovative ideas from across the organization in a structured manner.  Ideas with Less Immediate Usefulness:  For context and to provide a complete picture, I also considered the following concepts but believe they may offer less value at this time.      Mandatory "Innovation" Hours: Requiring a fixed block of time each week for unstructured creative thinking. While the intent is positive, it may feel forced and could disrupt focused work periods without a clear structure or objective.      Switching to a Niche Communication Tool: Adopting a new, unfamiliar internal messaging platform that offers features already available in our current, well-integrated suite of tools. This could lead to confusion, reduce adoption, and create unnecessary fragmentation in our communications.      Detailed Daily Stand-up Reports: Replacing our brief daily check-ins with a requirement for lengthy, written status reports. This would likely add significant administrative overhead without a commensurate increase in transparency or productivity.  My intention is simply to spark discussion. I am available at your convenience to elaborate on any of these points or to discuss other ways we might continue to improve our team's effectiveness.  Thank you for your time and consideration.  Best regards,  [Your Name] [Your Title]"""


print(os.environ['GEMINI_API_KEY'])


response = requests.post(
    "http://localhost:8000/api/IsUsefulEmail/",
    json={
        "email_content": email
    }
)
for a in response:
    print(a,a.index)