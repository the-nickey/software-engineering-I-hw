from transformers import MBartTokenizer, MBartForConditionalGeneration


def summarizer(text_to_summarize):
    model_name = "IlyaGusev/mbart_ru_sum_gazeta"
    tokenizer = MBartTokenizer.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name)

    input_ids = tokenizer(
        [text_to_summarize],
        max_length=600,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=4
    )[0]

    return tokenizer.decode(output_ids, skip_special_tokens=True)


if __name__ == '__main__':
    text = """
    В отличие от Data Scientist, Machine Learning Engineer гораздо чаще занимается внедрением модели в продакшен. Именно этим он и отличается от специалистов по обработке/анализу данных. На первый взгляд может показаться, что ML-инженер занимается только эксплуатацией моделей машинного обучения. Конечно, это не совсем так, инженер по машинному обучению может работать над оптимизацией алгоритмов машинного обучения, повышением их производительности, полностью перестраивать их. Некоторые (чаще маленькие) компании предпочитают всестороннего Data Scientist, который способен как работать с алгоритмами машинного обучения так и внедрять эти решения в продакшен. Но чем компания больше, с большей вероятностью предпочтут разделить эти две роли. Одному человеку может быть сложно сделать все от начала до конца, поэтому наличие двух специалистов, один из которых занимается построением модели, а другой — ее развертыванием, часто является более эффективным подходом.
    """
    print(summarizer(text))