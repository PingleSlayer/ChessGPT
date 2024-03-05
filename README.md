# ChessGPT

## Overview
This project aims to help create a versatile chess Language Model (LLM) capable of various tasks, from basic chess understanding to advanced tutoring.
I do not have the hardware nor the funds to create such a model myself, but I hope to help create some of the frameworks and the data for achieving this model. 
This project is only in its starting phase and is aimed to be an open-source community project, so if you have any ideas/tips feel free to contribute!

I believe a finalized model could outperform Stockfish while being able to thoroughly explain why it makes certain decisions. 

I think that a community should be capable of producing enough data and compute to create an amazing model and to serve as a proof of concept of some techniques for creating specialized models.
Some of the unique techniques I would like to test/use are:
 - Creating a wide variety of tasks to improve overal knowledge in the field
 - Using well-structured prompts for said tasks
 - Training in multiple stages on different types of data for specific improvements
 - Making use of hidden tokens used for reasoning that can be ignored during training/finetuning (both to improve performance and to be able to more effectively train on unlabled data?)

The plan outlines training levels, tasks, data collection, and possible model releases. 

## Use Cases

### Chess Tutor
One of my main drives for helping create this model is to be able to use it as a cost-effective expert level chess tutor. 
I've recently gotten into chess and I feel like having such a model at my hands could massively help me improve.
It could accurately and thorougly explain why certain moves are better than others, it could give feedback on my games, it could suggest what I should improve and much more.
Also the model could be made to tailor its explanations to specific people considering their age, elo, previous conversations,...

### Engine
Another use case for this model is as an engine.
Current engines at specific elo's feel very weird, they don't play at all like a human at that elo would.
This model could make very human-like moves at specific elo's.
I also believe that through the power of reason and memory we can get this model to outperform stockfish even at a relatively low parametercount.

### ELO-estimation,...
Other use cases could be:
- **elo-estimation:** which could be helpful for quickly analyzing a player's strength.
- ...

## Training Plan

### Plan
Here's a roadmap to transform ChessGPT from its inception to the ultimate chess companion:
- Choose and obtain an open-source pretrained LLM.
- Collect as much chess-related text data as possible.
- **Training 1:** Train model on data gathered in the previous step.
- Think of additional tasks and do prompt engineering on task prompts.
- Collect human written examples of tasks (Reasoning + Response).
- Generate variations of data using chatGPT or other methods.
- Translate this data to different languages.
- **Training 2:** Finetune model on the data collected in the previous 3 steps (Reasoning + Response for Tasks 0-22).
- **Release 1:** Use model for summarizing games, explaining basic moves, and answering chess trivia questions.
- **Training 3:** Train model on unlabeled data (Response only for Tasks 5-22).
- **Release 2:** Use model for evaluating positions, estimating ELO, predicting the next move, and as a chess engine at a specific ELO.
- **Training 4:** Perform RLHF on the model for checking/improving performance.
- **Release 3:** Use model as the alpha version of the chess tutor.
- Evaluate conversations ChessGPT had with users.
- **Training 5:** Train model on evaluation data from the previous step.
- **Release 4:** Use model as the beta version of the chess tutor.
- **Training 6:** Train model through playing games against itself (Response only for Tasks 5-11) + Train on unlabeled data (Response only for Tasks 12-22).
- **Release 5:** Use this version as a super strong chess engine.
- **Training 7:** Perform RLHF on the model to check/improve performance.
- **Release 6:** Use this version for super strong chess tutor

### Stages
ChessGPT's training will progress through distinct stages, each focusing on different data types.
- **Pretrained LLM:** Basic language understanding.
- **Pretrained Chess LLM:** Basic chess understanding.
- **Finetuned Chess LLM:** Mimic chess reasoning.
- **Improved Chess LLM:** Basic chess reasoning.
- **Alpha Chess Tutor LLM:** Basic chess tutoring.
- **Beta Chess Tutor LLM:** Improved chess tutoring.
- **Expert Chess Player LLM:** Super strong chess engine.
- **Expert Chess Tutor LLM:** Expert chess tutoring.

### Tasks
ChessGPT's capabilities will be refined through various tasks, including:
- **Teach chess effectively**
- **Answer chess trivia questions**
- **Find the best move**
- **Evaluate position**
- **Guess the ELO**
- **Predict next move**

### Reasoning
I suggest having the model always output its reasoning before giving its response. 
This would make the model slightly more expensive during inference, but I believe it could massively increase its performance.
Through the power of reason the performance of a smaller model should be similar to the performance of a much larger model making it more cost-effective overall.
At first we should train the model on examples that have both reasoning and response, later we should find a way to train the model only based on its response and not the reasoning.
This would mean we can train the model on a huge quantity of data for which we have no reasoning examples available.

## Data
Experimentation with diverse data collection methods is crucial for ChessGPT's success. We're exploring:
- **Manual writing:** the best way for gathering high-quality data (reasoning and response) is by manually writing it.
- **ChatGPT:** some tasks are simple enough that we can create high-quality synthetic data (reasoning and response or response only) by just using ChatGPT (examples: chess trivia Q&A,...).
- **Computer generated:** some of the tasks are so simple that we do not even need ChatGPT for creating the data (response only) (examples: find best move, evaluate position,...).
- **Lichess library:** for some tasks we can not simply generate the data locally but we could use the Lichess library to collect the data (response only) (examples: guess ELO, guess player, predict next move,...).
- **Self-play:** performance on some tasks could be improved by having the model play against itself* (response only) (examples: find best move, evaluate position,...)
- **RLHF:** for checking and improving the models capabilities we could perform some RLHF (reasoning and response)


Join us in shaping the future of ChessGPT and making chess knowledge accessible to all! Feel free to contribute and share your insights.
