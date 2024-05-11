from superjsonmode.integrations.openai import StructuredOpenAIModel
from pydantic import BaseModel
import time
import json

class LLMConverter:
    def __init__(self, schema_path):
        self.schema = self.load_schema(schema_path)
        self.model = StructuredOpenAIModel()
        self.prompt_template = self.get_prompt_template()

    def load_schema(self, schema_path):
        with open(schema_path, "r") as file:
            self.schema = json.load(file)
    
    def convert(self, input_content):
        output = self.model.default_generate(
            input_content,
            extraction_prompt_template=self.prompt_template,
            schema=self.schema,
            temperature=0,
        )
        return output
    
    def get_prompt_template(self):
        return """{prompt}

        Based on this excerpt, extract the correct value for the provided key. Do not miss any data. Create new keys as you please. It should be json.

         """

if __name__ == "__main__":
    converter = LLMConverter("llm_converter/schema.json")
    input_data = """Today, John Doe visited for his annual check-up, appearing in good health and spirits. At 45, he remains 
        active, balancing his work and personal life well. As a non-smoker who enjoys a casual drink now and then, 
        he's keen on maintaining his thrice-weekly exercise routine. His medical history is unremarkable except for an 
        appendectomy back in 2010, and thankfully, there are no new ailments to report. His vitals were stable and within 
        normal limits; a reassuring blood pressure of 120/80 mmHg, a steady heart rate of 72 bpm, and all other readings 
        including respiratory rate and temperature were normal. The physical exam showed a well-nourished individual with no 
        distress, clear lungs, a regular heartbeat, and a soft, non-tender abdomen. Lab results were equally reassuring with 
        cholesterol levels and blood glucose well managed. I advised John to keep up his healthy lifestyle and we agreed to 
        schedule his next visit a year from now. It's always a pleasure to see a patient so engaged in their health. """
    res = converter.convert(input_data)
    print(res)
    

# # Remember to set your OPENAI_API_KEY env variable
# # or pass in `api_key` to the constructor below
# 
# # Blueprint of the expected output
# MedicalReport = {
#     "name": "",
#     "age": "",
#     "lifestyle": "",
#     "medical_history": "",
#     "vitals": "",
#     "physical_exam": "",
#     "lab_results": "",
#     "notes": "",
# }

# prompt = """Today, John Doe visited for his annual check-up, appearing in good health and spirits. At 45, he remains 
# active, balancing his work and personal life well. As a non-smoker who enjoys a casual drink now and then, 
# he's keen on maintaining his thrice-weekly exercise routine. His medical history is unremarkable except for an 
# appendectomy back in 2010, and thankfully, there are no new ailments to report. His vitals were stable and within 
# normal limits; a reassuring blood pressure of 120/80 mmHg, a steady heart rate of 72 bpm, and all other readings 
# including respiratory rate and temperature were normal. The physical exam showed a well-nourished individual with no 
# distress, clear lungs, a regular heartbeat, and a soft, non-tender abdomen. Lab results were equally reassuring with 
# cholesterol levels and blood glucose well managed. I advised John to keep up his healthy lifestyle and we agreed to 
# schedule his next visit a year from now. It's always a pleasure to see a patient so engaged in their health. """

# start = time.time()
# output = model.generate(
#     prompt,
#     extraction_prompt_template=prompt_template,
#     schema=MedicalReport,
#     batch_size=6,
#     temperature=0,
# )
# print(f"Total time: {time.time() - start}")
# print(output)
#
# start = time.time()




# print(f"Total time: {time.time() - start}")

# print(output)

# with open("output.json", "w") as out_f:
#     out_f.write(output)

