from transformers import MarianMTModel, MarianTokenizer

# Simple cache to avoid reloading models on every call
_MODEL_CACHE = {}

def translate_text(text, target_lang):
    model_name = f"Helsinki-NLP/opus-mt-en-{target_lang}"
    try:
        if model_name not in _MODEL_CACHE:
            tokenizer = MarianTokenizer.from_pretrained(model_name)
            model = MarianMTModel.from_pretrained(model_name)
            _MODEL_CACHE[model_name] = (tokenizer, model)
        else:
            tokenizer, model = _MODEL_CACHE[model_name]

        translated = model.generate(
            **tokenizer(text, return_tensors="pt", padding=True)
        )

        return tokenizer.decode(translated[0], skip_special_tokens=True)
    except Exception:
        # If translation model is unavailable or fails, return original text
        return text