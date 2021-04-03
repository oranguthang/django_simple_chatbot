import React, {Component} from 'react';


class SendMessageForm extends Component {
    constructor() {
        super();
        this.state = {
            message: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleChange(e) {
        this.setState({
            message: e.target.value
        })
    }

    handleSubmit(e) {
        e.preventDefault();
        this.props.sendMessage(this.state.message, 'in');
        this.setState({
            message: ''
        });
        fetch("http://127.0.0.1:8000/get_next_question/?id=" + this.props.nextQuestionId +
            "&answer=" + this.state.message + "&uuid=" + this.props.uuid)
            .then(res => res.json())
            .then(
                (res) => {
                    if (res.name) {
                        this.props.setNextQuestionId(res.id);
                    }
                }
            )
    }

    render() {
        return (
            <form
                onSubmit={this.handleSubmit}
                className="send-message-form">
                <input
                    onChange={this.handleChange}
                    value={this.state.message}
                    placeholder="Message text"
                    type="text"/>
                <input
                    value="Send"
                    type="submit"/>
            </form>
        )
    }
}

export default SendMessageForm;