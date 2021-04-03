import React, {Component} from 'react';
import Title from './components/Title.js'
import MessageList from './components/MessageList.js'
import SendMessageForm from './components/SendMessageForm.js'
import './App.css';
import QuestionnaireSelector from "./components/QuestionnaireSelector";
import uuid from "uuid";


class App extends Component {
    constructor() {
        super();
        this.state = {
            messages: [],
            nextQuestionId: null,
            uuid: uuid.v4()
        };
        this.sendMessage = this.sendMessage.bind(this);
        this.setNextQuestionId = this.setNextQuestionId.bind(this);
    };

    sendMessage(message, type) {
        this.setState({
            messages: [...this.state.messages, {type: type, text: message}]
        });
    };

    setNextQuestionId(nextQuestionId) {
        this.setState({
            nextQuestionId: nextQuestionId
        });
        fetch("http://127.0.0.1:8000/get_question_with_answers/?id=" + nextQuestionId)
            .then(res => res.json())
            .then(
                (res) => {
                    this.sendMessage(res.text, 'out')
                }
            )
    }

    render() {
        let container;
        if (this.state.nextQuestionId) {
            container = (
                <React.Fragment>
                    <MessageList messages={this.state.messages}/>
                    <SendMessageForm
                        nextQuestionId={this.state.nextQuestionId}
                        uuid={this.state.uuid}
                        setNextQuestionId={this.setNextQuestionId}
                        sendMessage={this.sendMessage}/>
                </React.Fragment>
            )
        } else {
            container = (
                <QuestionnaireSelector
                    messages={this.state.messages}
                    setNextQuestionId={this.setNextQuestionId}/>
            )
        }

        return (
            <div className="app">
                <Title/>
                {container}
            </div>
        );
    }
}

export default App;
