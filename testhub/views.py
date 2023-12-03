from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def index(request):
    """View function for home page"""

    return (render(request, 'index.html'))


@login_required
def get_questions(request, question_id):
    """Method that get the questions from the data
        store the users response in a session
    """
    
    question = get_object_or_404(Question, pk=question_id)
    
    answers = Answer.objects.filter(question=question)

    
    #display nextbutton based on the question
    nextQuestion = Question.objects.filter(id__gt=question.id).order_by('id').first()
    #display prev button based on the question
    prevQuestion = Question.objects.filter(id__lt=question.id).order_by('-id').first()
    
    
    
    if request.method == 'POST':
        selected_answer_id = request.POST.get('selected_answer') 

        if selected_answer_id:

            selected_answer = get_object_or_404(Answer, pk=selected_answer_id)
            is_correct = selected_answer.is_correct
        
            #Create an empty list of users response
            user_responses = request.session.get('user_responses', [])
        
            user_responses.append(
                {
                    'question_id': question.id,
                    'selected_answer_id': selected_answer_id,
                    'is_correct': is_correct,
                }
            )
        
        
            request.session['user_responses'] = user_responses

            
            if nextQuestion:
                
                return (redirect('get_questions', question_id=nextQuestion.id))
            else:
                return(redirect("index"))        
        
        else:
            messages.error(request, "An Answer must be selected before you can continue.")



    return (render(request, 'quiz.html', {'question': question,
                                          'answers': answers,
                                          'prevQuestion': prevQuestion,
                                          'nextQuestion': nextQuestion,
                                          }))
    
    
    

@login_required
def review_quiz(request):
        """Method that display the quiz result"""
        
        #Get the user responses from the session
        user_responses = request.session.get('user_responses', [])
        
        
        #Calculate the score
        total_score = sum(1 for response in user_responses if response['is_correct'])
        
        #clear the session
        request.session['user_responses'] = []
        
        return (render(request, 'review.html',
                   {
                       'user_responses': user_responses,
                       'total_score': total_score,
                   }))
 
 
 
@login_required
def instruction(request):
     """Method that render the instruction page"""
     question_length = Question.objects.count()
     
     return(render(request, 'instruction.html', {
         'question_length': question_length,
    
     }))