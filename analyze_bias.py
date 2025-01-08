import openai
from typing import Dict, Tuple

def analyze_bias(data: Dict, context: str, demographic: str) -> Tuple[str, int]:
    """
    Analyzes data for potential bias against a demographic category using GPT-4.
    
    Args:
        data (Dict): Dictionary containing the data to analyze
        context (str): Summary of the context/purpose of the data
        demographic (str): The demographic category being analyzed for bias
        
    Returns:
        Tuple[str, int]: A tuple containing:
            - Explanation string of why the data is or isn't biased
            - Integer score from 0-100 indicating bias level (0 = no bias, 100 = extremely biased)
    """
    
    # Construct the prompt for the API
    prompt = f"""
    Please analyze the following data for potential bias against the specified demographic category.
    
    Data: {data}
    Context: {context}
    Demographic Category: {demographic}
    
    Analyze whether this data shows evidence of bias. Consider:
    1. Statistical representation
    2. Contextual factors
    3. Historical patterns
    4. Methodological fairness
    
    Provide:
    1. A concise explanation of whether bias exists and why
    2. A numerical score from 0-100 where 0 means no bias and 100 means extreme bias
    
    Format the response as: "EXPLANATION|SCORE"
    """
    
    try:
        # Make the API call
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert in data analysis and bias detection."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3  # Lower temperature for more consistent analysis
        )
        
        # Parse the response
        response_text = response.choices[0].message.content
        explanation, score_str = response_text.split("|")
        
        # Convert score to integer and validate
        score = int(float(score_str.strip()))
        score = max(0, min(100, score))  # Ensure score is between 0 and 100
        
        return explanation.strip(), score
        
    except Exception as e:
        return f"Error analyzing bias: {str(e)}", 0

def format_bias_report(explanation: str, score: int) -> str:
    """
    Formats the bias analysis results into a readable report.
    
    Args:
        explanation (str): The explanation of bias analysis
        score (int): The bias score (0-100)
        
    Returns:
        str: Formatted report
    """
    bias_level = "Low" if score < 33 else "Medium" if score < 66 else "High"
    
    report = f"""
    Bias Analysis Report
    -------------------
    Bias Level: {bias_level} ({score}%)
    
    Analysis:
    {explanation}
    """
    
    return report

# Example usage
# if __name__ == "__main__":
#     # Example data
#     sample_data = {
#         "department_hires": {
#             "engineering": {"male": 75, "female": 25},
#             "marketing": {"male": 45, "female": 55},
#             "sales": {"male": 60, "female": 40}
#         }
#     }
    
#     sample_context = "Annual hiring statistics for different departments in a tech company"
#     sample_demographic = "gender"
    
#     explanation, score = analyze_bias(sample_data, sample_context, sample_demographic)
#     report = format_bias_report(explanation, score)
#     print(report)