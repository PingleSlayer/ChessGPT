# ChessGPT

## Overview
This project aims to help create a versatile chess Language Model (LLM) capable of various tasks, from basic chess understanding to advanced tutoring.
I do not have the hardware nor the funds to create such a model myself, but I hope to help create some of the frameworks and the data for achieving this model. 

I believe a finalized model could outperform Stockfish while being able to thoroughly explain why it makes certain decisions. 

I believe that a community should be capable of producing enough data and compute to create an amazing model and to serve as a proof of concept of some techniques for creating specialized models.
Some of the unique techniques I would like to test/use are:
 - Creating a wide variety of tasks to improve overal knowledge in the field
 - Using well-structured prompts for tasks
 - Training in multiple stages for specific improvements
 - Making use of hidden tokens used for reasoning that can be ignored during training/finetuning (both to improve performance and to be able to more effectively train on unlabled data?)

The plan outlines training levels, tasks, data collection, and possible model releases. 

## Training Plan

### Plan
The current plan to go from zero to the ultimate ChessGPT is as follows:
1. Obtain pretrained LLM or train own LLM.
2. Collect as much chess-related text data as possible.
3. **Training 1:** Train model on data gathered in the previous step.
4. Think of additional tasks and do prompt engineering on task prompts.
5. Collect human written examples of tasks (Reasoning + Response).
6. Generate variations of data using chatGPT or other methods.
7. **Training 2:** Finetune model on collected data.
8. **Release 1:** Use model for summarizing games, explaining basic moves, and answering chess trivia questions (English only).
9. **Training 3:** Train model on unlabeled data (Response only for Tasks 6-22).
10. **Release 2:** Use model for evaluating positions, estimating ELO, predicting the next move, and as a chess engine at a specific ELO (English only).
11. Translate human-written examples to common languages.
12. **Training 4:** Finetune model on translated human-written examples.
13. **Release 3:** Use model for all tasks from Releases 1 and 2 but in multiple languages.
14. **Training 5:** Perform RLHF on the model for checking/improving performance.
15. **Release 4:** Use model as the alpha version of the chess tutor.
16. Evaluate conversations ChessGPT had with users.
17. **Training 6:** Train model on evaluation data from the previous step.
18. **Release 5:** Use model as the beta version of the chess tutor.
19. Consider making the model multi-agent.
20. **Training 7:** Train model through playing games against itself (Response only for Tasks 6-11) + Train on unlabeled data (Response only for Tasks 12-22).
21. **Release 6:** Use this version as a super strong chess engine.
22. **Training 8:** Perform RLHF on the model to check/improve performance.
23. **Release 7:** Use this version for super strong chess tutor

### Stages
There will be several stages of training that will use very different kinds of data. We can differentiate the following stages:
1. **Pretrained LLM:** Basic language understanding.
2. **Pretrained Chess LLM:** Basic chess understanding.
3. **Finetuned Chess LLM:** Mimic chess reasoning.
4. **Improved Chess LLM:** Basic chess reasoning.
5. **Multilingual Chess LLM:** Chess reasoning in multiple languages.
6. **Alpha Chess Tutor LLM:** Basic chess tutoring.
7. **Beta Chess Tutor LLM:** Improved chess tutoring.
8. **Expert Chess Player LLM:** Super strong chess engine.
9. **Expert Chess Tutor LLM:** Expert chess tutoring.

### Tasks
To improve the model's overal chess capabilties we have devised a variety of tasks. Some of the tasks we have constructed are:
1. **Teach chess effectively** 
2. **Answer chess trivia questions**
3. **Find the best move**
4. **Evaluate position**
5. **Guess the ELO**
6. **Predict next move** 

### Data
We are experimenting with different techniques for collecing the required data for the training of ChessGPT. The following methods are being tried:
1. **Manual writing:** the best way for gathering high-quality data (reasoning and response) is by manually writing it.
2. **ChatGPT:** some tasks are simple enough that we can create high-quality synthetic data (reasoning and response or response only) by just using ChatGPT (examples: chess trivia Q&A,...).
3. **Computer generated:** some of the tasks are so simple that we do not even need ChatGPT for creating the data (response only) (examples: find best move, evaluate position,...).
4. **Lichess library:** for some tasks we can not simply generate the data locally but we could use the Lichess library to collect the data (response only) (examples: guess ELO, guess player, predict next move,...).
5. **Self-play:** performance on some tasks could be improved by having the model play against itself* (response only) (examples: find best move, evaluate position,...)

